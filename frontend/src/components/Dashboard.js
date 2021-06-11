import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import PlayerContext from '../utils/PlayerContext';

const Dashboard = () => {
    const player = useContext(PlayerContext)

    if (!player.id) {
        return <h3>Loading...</h3>
    }

    const leagueNodes = player.leagues.map(league => {
        return <li key={league.id}>
            <Link to = {"/leagues/" + league.id}>
                {league.name}
            </Link>
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
            <h4>Last Match + your prediction</h4>
            <h4>Next Match + your prediction</h4>
        </>
    )
}

export default Dashboard;