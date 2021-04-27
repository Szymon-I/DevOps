import React, { useEffect, useState, Fragment } from "react";
import type { Pokemon } from "../types/pokemon.tsx";
import { API_URL_ALL_POKEMONS } from "../constants.tsx";

const PokemonListView = () => {
  const [pokemons, setPokemons] = useState<Pokemon[]>([]);

  /** Fetch first batch of pokemons into app state on component load */
  const initPopulate = (): undefined => {
    fetch(API_URL_ALL_POKEMONS)
      .then(
        (response) => response.json(),
        (errors) => console.log(errors)
      )
      .then((json) => {
        setPokemons(json);
      });
  };

  /** Run functions on component load */
  useEffect(() => {
    if (!pokemons || !pokemons.length) {
      initPopulate();
    }
  });

  /** Render pokemon names in list div form */
  const renderPokemons = () => {
    return !!pokemons ? (
      pokemons.map((pokemon, id) => <div key={id}>{pokemon.name}</div>)
    ) : (
      <Fragment />
    );
  };

  return <div>{renderPokemons()}</div>;
};

export { PokemonListView };
