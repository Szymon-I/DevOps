import React, { useEffect, useState, Fragment } from "react";
import { API_URL_ALL_POKEMONS } from "../constants.tsx";
import { useParams } from "react-router-dom";
import { getPokemonDict } from "../utils.ts";

const PokemonDetailView = () => {
  const { id } = useParams();
  const [pokemon, setPokemon] = useState<Pokemon>(null);
  const [newPokemon, setNewPokemon] = useState<Pokemon>(null);

  /** Fetch pokemon details into app state on component load */
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
  useEffect((): undefined => {
    if (!pokemon) {
      initPopulate();
    }
  });

  /** Render pokemon */
  const renderPokemon = (): React.StatelessComponent<{}> => {
    return !!pokemon && !("detail" in pokemon) ? (
      <table>
        <tbody>
          <th>property</th>
          <th>value</th>
          <th>new value</th>
          {Object.keys(pokemon).map((property, id) => (
            <tr key={id}>
              <td>{property}</td>
              <td>{pokemon[property]}</td>
              <td></td>
            </tr>
          ))}
        </tbody>
      </table>
    ) : (
      // <div>{pokemon.name}</div>
      <div>Not found</div>
    );
  };

  return <Fragment>{renderPokemon()}</Fragment>;
};

export { PokemonDetailView };
