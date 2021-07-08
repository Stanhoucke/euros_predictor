import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import PlayerContext from '../utils/PlayerContext';

const Dashboard = ({matchPredictionComparison}) => {
    const player = useContext(PlayerContext)

    if (!player.id) {
        return <div className="d-flex flex-column align-items-center">
            <strong className="h3 mb-4 text-primary">Loading...</strong>
            <div className="spinner-border text-primary" role="status" aria-hidden="true" style={{width: '3em', height: '3em'}}></div>
        </div>
    }

    const leagueNodes = player.leagues.map(league => {
        return <li key={league.id} className="list-group-item bg-light">
            <Link to = {"/leagues/" + league.id}>
                {league.name}
            </Link>
        </li>
    })

    return (
        <div className="container">
            <h3>Dashboard</h3>
            <div className="list-group-item bg-light d-flex justify-content-between align-items-start mb-5" key={player.id}>
                <div className="ms-2 me-auto d-flex flex-column align-items-baseline">
                    <div className="fw-bold">
                        <p className="mb-0">{player.team_name}</p>
                    </div>
                    <small className="fst-italic">{player.first_name} {player.last_name}</small>
                </div>
                <p className="fw-bold fs-3 mb-0 badge bg-success" style={{width: 3 + 'em'}}>{player.points}</p>
            </div>


            <h4>Leagues</h4>
            <ul className="list-group mb-5">
                {leagueNodes}
            </ul>

            {matchPredictionComparison}
        </div>
    )
}

export default Dashboard;