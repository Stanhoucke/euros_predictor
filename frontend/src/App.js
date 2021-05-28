import React, { useEffect, useState } from 'react';
import {BrowserRouter as Router, Link, Route, Switch} from 'react-router-dom';
import './App.css';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import Home from './containers/Home';
import Request from './helpers/Request';

function App() {
  const [token, setToken] = useState();

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
  
  if(!token) {
    return <Login setToken={setToken}/>
  }

  return (
    <div className="App">
      <h1>Euros Predictor</h1>
      <Router>
        <Link to={"/"}>Home</Link>
        <Link to={"/dashboard"}>Dashboard</Link>
        <Switch>
          <Route path="/dashboard" render={() => {
            return <Dashboard/>
          }} />
          <Route render={() => {
            return <Home
              teams={teams}/>
          }} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
