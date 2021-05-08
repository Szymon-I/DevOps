from typing import List

from aioredis import Redis
from sqlalchemy.orm import Session

from src.consts.api_consts import API_LIMIT, API_SKIP
from src.pokemon import schema
from src.pokemon.models import Pokemon


def get_all_pokemons(
    db: Session, skip: int = API_SKIP, limit: int = API_LIMIT
) -> List[schema.Pokemon]:
    """ Return list of pokemons with pagination arguments """

    return db.query(Pokemon).offset(skip).limit(limit).all()


def get_pokemon(db: Session, pokemon_id: int) -> schema.Pokemon:
    """ Return pokemon based on primary key """

    return db.query(Pokemon).get(pokemon_id)


async def delete_pokemon(db: Session, pokemon_id: int, cache: Redis) -> None:
    """ Delete pokemon based on primary key """

    await cache.delete(f"pokemon_{pokemon_id}")
    await cache.delete("pokemons")

    deleted = db.query(Pokemon).get(pokemon_id)
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id)
    pokemon.delete()
    db.commit()
    return deleted
