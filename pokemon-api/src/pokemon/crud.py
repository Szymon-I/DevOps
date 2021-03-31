from typing import List

from sqlalchemy.orm import Session

from src.consts.api_consts import API_LIMIT, API_SKIP
from src.pokemon import models, schema


def get_all_pokemons(
    db: Session, skip: int = API_SKIP, limit: int = API_LIMIT
) -> List[schema.Pokemon]:
    """ Return list of pokemons with pagination arguments """
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def get_pokemon(db: Session, pokemon_id: int) -> schema.Pokemon:
    """ Return pokemon based on primary key """
    return db.query(models.Pokemon).get(pokemon_id)
