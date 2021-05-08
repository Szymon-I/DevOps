import React, { useEffect, useState, Fragment, useCallback } from "react";
import type { Pokemon } from "../types/pokemon.tsx";
import { API_URL_ALL_POKEMONS } from "../constants.tsx";
import { useHistory } from "react-router-dom";

const PokemonListView = () => {
  const [pokemons, setPokemons] = useState<Pokemon[]>([]);
  const history = useHistory();

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
    initPopulate();
  }, []);

  /** Delete pokemon from db */
  const deletePokemon = (primary_key: number, array_id: number) => {
    fetch(API_URL_ALL_POKEMONS + primary_key, {
      method: "DELETE",
    }).then((response) => console.log(response.json()));
    const newPokemonArray = pokemons.filter((name, j) => array_id !== j);
    setPokemons(newPokemonArray);
  };

  /** Redirect to pokemon detail view */
  const redirectDetailView = (id: number) => {
    history.push(`/detailView/${id}`);
  };

  /** Render pokemon names in list form */
  const renderPokemons = () => {
    return !!pokemons ? (
      <table>
        <tbody>
          {pokemons.map((pokemon, id) => (
            <tr key={id}>
              <td>{pokemon.id}</td>
              <td>{pokemon.name}</td>
              <td>
                <button
                  onClick={() => {
                    deletePokemon(pokemon.id, id);
                  }}
                >
                  delete
                </button>
              </td>
              <td>
                <button
                  onClick={() => {
                    redirectDetailView(pokemon.id);
                  }}
                >
                  detail
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    ) : (
      <Fragment />
    );
  };

  return <div>{renderPokemons()}</div>;
};

export { PokemonListView };
