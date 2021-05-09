from typing import Optional

from pydantic import BaseModel


class Pokemon(BaseModel):
    id: Optional[int]
    pokedex_number: Optional[int]
    name: Optional[str]
    german_name: Optional[str]
    japanese_name: Optional[str]
    generation: Optional[int]
    is_sub_legendary: Optional[bool]
    is_legendary: Optional[bool]
    is_mythical: Optional[bool]
    species: Optional[str]
    type_number: Optional[int]
    type_1: Optional[str]
    type_2: Optional[str]
    height_m: Optional[float]
    weight_kg: Optional[float]
    abilities_number: Optional[int]
    ability_1: Optional[str]
    ability_2: Optional[str]
    ability_hidden: Optional[str]
    total_points: Optional[int]
    hp: Optional[int]
    attack: Optional[int]
    defense: Optional[int]
    sp_attack: Optional[int]
    sp_defense: Optional[int]
    speed: Optional[int]
    catch_rate: Optional[int]
    base_friendship: Optional[int]
    base_experience: Optional[int]
    growth_rate: Optional[str]
    egg_type_number: Optional[int]
    egg_type_1: Optional[str]
    egg_type_2: Optional[str]
    percentage_male: Optional[float]
    egg_cycles: Optional[float]
    against_normal: Optional[float]
    against_fire: Optional[float]
    against_water: Optional[float]
    against_electric: Optional[float]
    against_grass: Optional[float]
    against_ice: Optional[float]
    against_fight: Optional[float]
    against_poison: Optional[float]
    against_ground: Optional[float]
    against_flying: Optional[float]
    against_psychic: Optional[float]
    against_bug: Optional[float]
    against_rock: Optional[float]
    against_ghost: Optional[float]
    against_dragon: Optional[float]
    against_dark: Optional[float]
    against_steel: Optional[float]
    against_fairy: Optional[float]

    class Config:
        orm_mode = True


schema_extra = {
    "example": {
        "id": 2,
        "pokedex_number": 2,
        "name": "Ivysaur",
        "german_name": "Bisaknosp",
        "japanese_name": "フシギソウ (Fushigisou)",
        "generation": 1,
        "is_sub_legendary": False,
        "is_legendary": False,
        "is_mythical": False,
        "species": "Seed Pokémon",
        "type_number": 2,
        "type_1": "Grass",
        "type_2": "Poison",
        "height_m": 1.0,
        "weight_kg": 13.0,
        "abilities_number": 2,
        "ability_1": "Overgrow",
        "ability_2": None,
        "ability_hidden": "Chlorophyll",
        "total_points": 405,
        "hp": 60,
        "attack": 62,
        "defense": 63,
        "sp_attack": 80,
        "sp_defense": 80,
        "speed": 60,
        "catch_rate": 45,
        "base_friendship": 70,
        "base_experience": 142,
        "growth_rate": "Medium Slow",
        "egg_type_number": 2,
        "egg_type_1": "Grass",
        "egg_type_2": "Monster",
        "percentage_male": 87.5,
        "egg_cycles": 20.0,
        "against_normal": 1.0,
        "against_fire": 2.0,
        "against_water": 0.5,
        "against_electric": 0.5,
        "against_grass": 0.25,
        "against_ice": 2.0,
        "against_fight": 0.5,
        "against_poison": 1.0,
        "against_ground": 1.0,
        "against_flying": 2.0,
        "against_psychic": 2.0,
        "against_bug": 1.0,
        "against_rock": 1.0,
        "against_ghost": 1.0,
        "against_dragon": 1.0,
        "against_dark": 1.0,
        "against_steel": 1.0,
        "against_fairy": 0.5,
    }
}
