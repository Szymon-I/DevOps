import os

import pandas as pd

from src.database import SessionLocal, engine
from src.pokemon.models import Pokemon


def dump_csv_to_db() -> None:
    """ Load data from csv and save into db """

    session = SessionLocal()
    if bool(session.query(Pokemon).first()):
        return

    int_bool_columns = ["is_sub_legendary", "is_legendary", "is_mythical"]
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "../../dump/pokedex.csv")
    df = pd.read_csv(file_path, index_col=0)
    for column in int_bool_columns:
        df[column] = df[column].astype(bool)
    df.to_sql(Pokemon.__name__, con=engine, if_exists="append", index=False)


if __name__ == "__main__":
    dump_csv_to_db()
