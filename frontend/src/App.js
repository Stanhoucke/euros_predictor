import React, { useEffect, useState } from 'react';
import {BrowserRouter as Router, Link, Route, Switch, useHistory} from 'react-router-dom';
import './App.css';
import AlertComponent from './components/AlertComponent';
import CreateLeague from './components/CreateLeague';
import Dashboard from './components/Dashboard';
import JoinLeague from './components/JoinLeague';
import LeagueDetails from './components/LeagueDetails';
import Leagues from './components/Leagues';
import Login from './components/Login';
import MatchPredictionComparison from './components/MatchPredictionComparison';
import NavBar from './components/NavBar';
import Register from './components/Register';
import useToken from './components/UseToken';
import Home from './containers/Home';
import Predictions from './containers/Predictions';
import Request from './helpers/Request';
import { PlayerProvider } from './utils/PlayerContext';
import PrivateRoute from './utils/PrivateRoute';

function App() {
  let history = useHistory();
  const { token, setToken } = useToken();
  const [errorMessage, setErrorMessage] = useState(null);

  const [groups, setGroups] = useState([]);
  const [activePlayer, setActivePlayer] = useState([]);
  const [showLeagueForms, setShowLeagueForms] = useState({
    "join-league": false,
    "create-league": false
  });
  const [previousMatch, setPreviousMatch] = useState({});
  const [nextMatch, setNextMatch] = useState({});

  const request = new Request();

  useEffect (() => {
    getGroups();
  }, [])
  useEffect (() => {
    if (token) {
      getActivePlayer();
    }
  }, [token])
  useEffect (() => {
    if (activePlayer.id) {
      setNextAndPreviousMatches();
    }
  }, [activePlayer])

  const getGroups = () => {
    request.get("/api/groups")
    .then(data => setGroups(data))
  }

  const getActivePlayer = () => {
    request.authGet("/api/player", token)
    .then(data => {
      if (data.status === "fail") {
        handleLogout()
      } else {
        setActivePlayer(data)
      }
    })
    .catch((error) => {
      console.log(error)
    })
  }
  
  const handleLogout = () => {
    request.authPost("http://localhost:5000/api/logout", {}, token)
    .then((res) => {
      localStorage.clear()
      // setToken(null)
      setErrorMessage(res.message)
      window.location = ("/login")
    })
  }

  const handleSubmitPredictions = (playerPredictions, event) => {
    event.preventDefault();
    
    request.put("/api/predictions", playerPredictions, token)
    .then((res) => {
      getActivePlayer();
      setErrorMessage(res.message)
    })
  }

  const handleCreateLeague = (leagueName, event) => {
    event.preventDefault();

    if (leagueName.name.length < 3) {
      setErrorMessage("League name must be at least 3 characters.")
    } else {
      request.authPost("/api/player_leagues", leagueName, token)
      .then((res) => {
        getActivePlayer();
        setErrorMessage(res.message)
      })
    }

  }
  const handleJoinLeague = (joinCode, event) => {
    event.preventDefault();

    if (joinCode.join_code.length !== 9) {
      setErrorMessage("Invalid league code.")
    } else {
      request.authPost("/api/player_leagues/join", joinCode, token)
      .then((res) => {
        getActivePlayer();
        setErrorMessage(res.message)
      })
    }
  }

  const toggleShowLeagueForm = (event) => {
    const {id} = event.target
    const reset = {
      "join-league": false,
      "create-league": false
    }
    if (showLeagueForms[id]) {
      setShowLeagueForms(reset)
    } else {
      reset[id] = true
      setShowLeagueForms(reset)
    }
  }

  const findLeagueById = (id) => {
    if (activePlayer.id) {
      return activePlayer.leagues.find((league) => {
        return league.id === parseInt(id);
      })
    }
  }

  const setNextAndPreviousMatches = () => {
    const today = new Date()
    const matches = []

    for (let [round_key, round_name] of Object.entries(activePlayer.predictions)) {
      for (let match of round_name){
        matches.push(match)
      }
    }

    for (let i = 1; i < matches.length; i++) {
        let matchDate = new Date(matches[i - 1].match.date)
        let nextMatchDate = new Date(matches[i].match.date)

        if (matchDate < today && nextMatchDate > today) {
            setPreviousMatch(matches[i - 1])
            setNextMatch(matches[i])
            break;
            
        }
    }
}

  const leagueForms = (
    <>
      <JoinLeague handleJoinLeague={handleJoinLeague} toggleShowLeagueForm={toggleShowLeagueForm} showForm={showLeagueForms["join-league"]}/>
      <CreateLeague handleCreateLeague={handleCreateLeague} toggleShowLeagueForm={toggleShowLeagueForm} showForm={showLeagueForms["create-league"]}/>
    </>
  )

  const matchPredictionComparison = (
    <>
      <MatchPredictionComparison match={previousMatch} title="Last Match"/>
      <MatchPredictionComparison match={nextMatch} title="Next Match"/>
    </>
  )

  return (
    <div className="App">
      <h1>Euros Predictor</h1>

      <Router>
        <NavBar token={token} handleLogout={handleLogout}/>
        
        <Switch>
          <Route exact path = "/" render={() => {
            return <Home
              groups={groups}/>
          }} />
          <Route path="/register" render={() => {
            return <Register setErrorMessage={setErrorMessage} setToken={setToken}/>
          }} />
          <Route path="/login" render={() => {
            return <Login setErrorMessage={setErrorMessage} setToken={setToken}/>
          }} />

          <PlayerProvider value={activePlayer}>
            <PrivateRoute path="/dashboard">
              <Dashboard matchPredictionComparison={matchPredictionComparison}/>
            </PrivateRoute>

            <PrivateRoute path="/predictions">
              <Predictions setErrorMessage={setErrorMessage} handleSubmitPredictions={handleSubmitPredictions}/>
            </PrivateRoute>
            
            <PrivateRoute exact path="/leagues/:id">
              <LeagueDetails findLeagueById={findLeagueById}/>
            </PrivateRoute>
            <PrivateRoute exact path="/leagues">
              <Leagues setErrorMessage={setErrorMessage} leagueForms={leagueForms}/>
            </PrivateRoute>

          </PlayerProvider>

        </Switch>
        <AlertComponent errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
      </Router>
    </div>
  );
}

export default App;
