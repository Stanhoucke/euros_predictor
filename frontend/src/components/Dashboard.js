import React, { useEffect } from 'react';

const Dashboard = ({getActivePlayer, activePlayer}) => {

    // useEffect (() => {
    //     getActivePlayer();
    //   }, [])

      const leagueNodes = activePlayer.leagues.map(league => {
          return <li key={league.id}>
                {league.name}
            </li>
      })

    return (
        <>
            <h3>Dashboard</h3>
            <h4>{activePlayer.first_name} {activePlayer.last_name}</h4>
            <h4>Points: {activePlayer.points}</h4>

            <h4>Leagues</h4>
            <ul>
                {leagueNodes}
            </ul> 
        </>
    )
}

export default Dashboard;