import React, { useEffect, useState } from 'react';
import {BrowserRouter as Router, Link, Route, Switch} from 'react-router-dom';
import './App.css';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import useToken from './components/UseToken';
import Home from './containers/Home';
import Request from './helpers/Request';
import PrivateRoute from './utils/PrivateRoute';

function App() {
  const { token, setToken } = useToken();

  const [teams, setTeams] = useState([]);
  const [activePlayer, setActivePlayer] = useState([]);

  const request = new Request();

  useEffect (() => {
    getTeams();
  }, [])

  const getTeams = () => {
    request.get("/api/teams")
    .then(data => setTeams(data))
  }

  return (
    <div className="App">
      <h1>Euros Predictor</h1>
      <Router>
        <Link to={"/"}>Home</Link>
        <Link to={"/dashboard"}>Dashboard</Link>
        <Link to={"/login"}>Login</Link>
        <Switch>
          <Route path="/login" render={() => {
            return <Login setToken={setToken}/>
          }} />
          <PrivateRoute path="/dashboard">
            <Dashboard/>
          </PrivateRoute>

          <Route exact path = "/" render={() => {
            return <Home
              teams={teams}/>
          }} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
