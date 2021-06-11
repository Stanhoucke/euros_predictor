import React, { useContext } from 'react';
import PlayerContext from '../utils/PlayerContext';

const LeaguePlayer = ({players}) => {
    const player = useContext(PlayerContext)

    const leaguePlayers = players.map((player, index) => {
        return <div key={player.id}>
            <p>Rank: {index + 1}</p>
            <p>{player.team_name}</p>
            <p>{player.points}</p>
            <small>{player.first_name} {player.last_name}</small>
        </div>
    })

    return (
        <>
            {leaguePlayers}
        </>
    )
}

export default LeaguePlayer;