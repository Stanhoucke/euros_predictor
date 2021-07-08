import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import PlayerContext from '../utils/PlayerContext';

const Leagues = ({leagueForms}) => {
    const player = useContext(PlayerContext)

    if (!player.id) {
        return <div className="d-flex flex-column align-items-center">
            <strong className="h3 mb-4 text-primary">Loading...</strong>
            <div className="spinner-border text-primary" role="status" aria-hidden="true" style={{width: '3em', height: '3em'}}></div>
        </div>
    }

    const leagueNodes = player.leagues.map((league) => {
        return <li key={league.id} className="list-group-item d-flex justify-content-between align-items-start">
            <div className="ms-2 me-auto">
                <div className="fw-bold">
                    <Link to = {"/leagues/" + league.id}>
                        {league.name}
                    </Link>
                </div>
            </div>
                <span className="badge bg-light text-dark me-4">Members: {league.players.length}</span>
                <span className="badge bg-primary">Rank: {league.players.findIndex(leaguePlayer => leaguePlayer.id === player.id) + 1}</span>
        </li>
    })

    return (
        <>
            {leagueForms}
            <h3 className="mt-5 mb-3">My Leagues</h3>
            <div className="container">
                <ul className="list-group list-group-flush">
                    {leagueNodes}
                </ul>
            </div>
        </>
    )
}

export default Leagues;