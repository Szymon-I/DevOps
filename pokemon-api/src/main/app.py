from typing import List, Dict
import pickle
from fastapi import Depends, FastAPI, Request, Response, HTTPException
from sqlalchemy.orm import Session

import src.pokemon.models as pokemon_models
from src.consts.api_consts import API_LIMIT, API_SKIP
from src.database import SessionLocal, engine
from src.pokemon import crud
from src.pokemon.schema import Pokemon as PokemonSchema
from src.utils.create_pokemon_db import dump_csv_to_db
from src.utils.main_utils import get_db, AppSettings
from src.utils.cache import get_cached_or_db
from aiocache import cached, Cache
from aiocache.serializers import PickleSerializer
from src.main.settings import DEFAULT_HOST, REDIS_PORT
import fastapi_plugins
from aioredis import Redis
from aiocache import caches


# Apply migrations to db and populate it
pokemon_models.Base.metadata.create_all(bind=engine)
dump_csv_to_db()

# init config and app
config = AppSettings()
app = FastAPI()


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
