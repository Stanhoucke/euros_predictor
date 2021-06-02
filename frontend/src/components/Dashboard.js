import React, { useContext } from 'react';
import PlayerContext from '../utils/PlayerContext';

const Dashboard = () => {
    const player = useContext(PlayerContext)

    const leagueNodes = player.leagues.map(league => {
        return <li key={league.id}>
            {league.name}
        </li>
    })

    return (
        <>
            <h3>Dashboard</h3>
            <h4>{player.first_name} {player.last_name}</h4>
            <h4>Points: {player.points}</h4>

            <h4>Leagues</h4>
            <ul>
                {leagueNodes}
            </ul> 
        </>
    )
}

export default Dashboard;