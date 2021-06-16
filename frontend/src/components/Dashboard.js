import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import PlayerContext from '../utils/PlayerContext';

const Dashboard = () => {
    const player = useContext(PlayerContext)

    if (!player.id) {
        return <h3>Dashboard Loading...</h3>
    }

    const lastMatch = () => {
        const today = new Date()

        for (let [index, round_name] of Object.entries(player.predictions)) {
            for (let i = 1; i < round_name.length; i++) {
                let matchDate = new Date(round_name[i - 1].match.date)
                let nextMatchDate = new Date(round_name[i].match.date)
                if (matchDate < today && nextMatchDate > today) {
                    console.log(round_name[i - 1].match.team_1.name)
                    break;

                    // Do both last and next match in same function?
                    // Move to app and pass prop to Dashboard?
                }
            }
        }
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

            <button onClick={lastMatch}>Last Match</button>

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