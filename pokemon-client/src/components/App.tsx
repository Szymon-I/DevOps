import "bootstrap/dist/css/bootstrap.css";
import logo from "../static/logo.svg";
import "../styles/App.css";
import React, { useEffect, useState } from "react";
import { PokemonListView } from "./pokemonListView.tsx";
import { PokemonDetailView } from "./pokemonDetailView.tsx";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useParams,
} from "react-router-dom";

const App = () => {
  useEffect(() => {
    document.title = "Pokemon App";
  })

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
          </ul>
        </nav>
        <Switch>
          <Route path="/detailView/:id" children={<PokemonDetailView />} />
          <Route path="/">
            <PokemonListView />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
