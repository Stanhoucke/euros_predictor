import React, { useEffect, useState } from 'react';
import {BrowserRouter as Router, Link, Route, Switch} from 'react-router-dom';
import './App.css';
import AlertComponent from './components/AlertComponent';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import NavBar from './components/NavBar';
import useToken from './components/UseToken';
import Home from './containers/Home';
import Request from './helpers/Request';
import PrivateRoute from './utils/PrivateRoute';

function App() {
  const { token, setToken } = useToken();
  const [errorMessage, setErrorMessage] = useState(null);

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

  const handleLogout = () => {
    request.authPost("http://localhost:5000/api/logout", {}, token)
    .then((res) => {
        if (res.status === "success"){
          localStorage.clear()
          setToken(null)
        }
        setErrorMessage(res.message)
    })
}

  return (
    <div className="App">
      <h1>Euros Predictor</h1>
      <Router>
        <NavBar token={token} handleLogout={handleLogout}/>
        
        <Switch>
          <Route path="/login" render={() => {
            return <Login setErrorMessage={setErrorMessage} setToken={setToken}/>
          }} />
          <PrivateRoute path="/dashboard">
            <Dashboard/>
          </PrivateRoute>

          <Route exact path = "/" render={() => {
            return <Home
              teams={teams}/>
          }} />
        </Switch>
        <AlertComponent errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
      </Router>
    </div>
  );
}

export default App;
