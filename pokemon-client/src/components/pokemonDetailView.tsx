import React, { useEffect, useState, Fragment } from "react";
import { API_URL_ALL_POKEMONS } from "../constants.tsx";
import { useParams } from "react-router-dom";
const PokemonDetailView = () => {
  const { id } = useParams();
  const [pokemon, setPokemon] = useState<Pokemon>(null);
  /** Fetch first batch of pokemons into app state on component load */
  const initPopulate = (): undefined => {
    fetch(API_URL_ALL_POKEMONS + id)
      .then(
        (response) => response.json(),
        (errors) => console.log(errors)
      )
      .then((json) => {
        setPokemon(json);
      });
  };

  /** Run functions on component load */
  useEffect(() => {
    if (!pokemon) {
      initPopulate();
    }
  });

  /** Render pokemon */
  const renderPokemon = () => {
    return !!pokemon ? <div>{pokemon.name}</div> : <Fragment />;
  };

  return <h2>{renderPokemon()}</h2>;
};

export { PokemonDetailView };
