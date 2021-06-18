from typing import List

import fastapi_plugins
import uvicorn
from aioredis import Redis
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse

import src.pokemon.models as pokemon_models
from sqlalchemy.orm import Session
from src.consts.api_consts import API_LIMIT, API_SKIP, API_PREFIX
from src.database import SessionLocal, engine
from src.main.settings import DEFAULT_HOST, DEFAULT_HOST_PORT
from src.pokemon import crud
from src.pokemon.schema import Pokemon as PokemonSchema
from src.utils.cache import get_cached_or_db
from src.utils.create_pokemon_db import dump_csv_to_db
from src.utils.main_utils import AppSettings, get_db

# Apply migrations to db and populate it
pokemon_models.Base.metadata.create_all(bind=engine)
dump_csv_to_db()

# init config and app
config = AppSettings()
app = FastAPI(root_path="/api")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    """ Middleware to assign db session for incoming request """
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.on_event("startup")
async def on_startup() -> None:
    await fastapi_plugins.redis_plugin.init_app(app, config=config)
    await fastapi_plugins.redis_plugin.init()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await fastapi_plugins.redis_plugin.terminate()


@app.get("/pokemon/", response_model=List[PokemonSchema])
async def get_pokemons(
    skip: int = API_SKIP,
    limit: int = API_LIMIT,
    db: Session = Depends(get_db),
    cache: Redis = Depends(fastapi_plugins.depends_redis),
):
    return await get_cached_or_db(
        cache=cache,
        cache_key="pokemons",
        query_function=lambda: crud.get_all_pokemons(db=db, skip=skip, limit=limit),
    )


@app.get("/pokemon/{pokemon_id}", response_model=PokemonSchema)
async def get_pokemon(
    pokemon_id: int,
    db: Session = Depends(get_db),
    cache: Redis = Depends(fastapi_plugins.depends_redis),
):
    """ Return specific pokemon by primary key """
    pokemon = await get_cached_or_db(
        cache=cache,
        cache_key=f"pokemon_{pokemon_id}",
        query_function=lambda: crud.get_pokemon(db=db, pokemon_id=pokemon_id),
    )

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon


@app.put("/pokemon/{pokemon_id}")
async def update_pokemon(
    pokemon_data: PokemonSchema,
    pokemon_id: int,
    db: Session = Depends(get_db),
):
    print(pokemon_data)
    crud.update_pokemon(db=db, pokemon_id=pokemon_id, data=pokemon_data)
    if True:
        return JSONResponse(status_code=200)
    return JSONResponse(status_code=404)


@app.delete("/pokemon/{pokemon_id}")
async def delete_pokemon(
    pokemon_id: int,
    db: Session = Depends(get_db),
    cache: Redis = Depends(fastapi_plugins.depends_redis),
):
    deleted = await crud.delete_pokemon(db=db, pokemon_id=pokemon_id, cache=cache)
    if deleted:
        return JSONResponse(status_code=200)
    return JSONResponse(status_code=404)


@app.get("/ping")
async def pong():
    return "pong"


if __name__ == "__main__":
    uvicorn.run(app, host=DEFAULT_HOST, port=DEFAULT_HOST_PORT)
