from typing import List

from fastapi import Depends, FastAPI, Request, Response
from sqlalchemy.orm import Session

import src.pokemon.models as pokemon_models
from src.consts.api_consts import API_LIMIT, API_SKIP
from src.database import SessionLocal, engine
from src.pokemon import crud
from src.pokemon.schema import Pokemon as PokemonSchema
from src.utils.create_pokemon_db import dump_csv_to_db
from src.utils.main_utils import get_db

# Apply migrations to db and populate it
pokemon_models.Base.metadata.create_all(bind=engine)
dump_csv_to_db()

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/pokemon/", response_model=List[PokemonSchema])
async def get_pokemons(
    skip: int = API_SKIP, limit: int = API_LIMIT, db: Session = Depends(get_db)
):
    return crud.get_all_pokemons(db=db, skip=skip, limit=limit)


@app.get("/pokemon/{pokemon_id}", response_model=PokemonSchema)
async def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    return crud.get_pokemon(db=db, pokemon_id=pokemon_id)
