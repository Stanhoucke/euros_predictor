import React from 'react';

const LeaguePlayer = ({players}) => {
    const leaguePlayers = players.map((player, index) => {
        return <li className="list-group-item bg-light d-flex justify-content-between align-items-start" key={player.id}>
            <p className="me-3 fw-bold">{index + 1}</p>
            <div className="ms-2 me-auto d-flex flex-column align-items-baseline">
                <div className="fw-bold">
                    <p className="mb-0">{player.team_name}</p>
                </div>
                <small className="fst-italic">{player.first_name} {player.last_name}</small>
            </div>
            <p className="fw-bold fs-3 mb-0 badge bg-success" style={{width: 3 + 'em'}}>{player.points}</p>
        </li>
    })

    return (
        <>
            {leaguePlayers}
        </>
    )
}

export default LeaguePlayer;