import React, { useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import PlayerContext from '../utils/PlayerContext';

const Leagues = () => {
    const player = useContext(PlayerContext)

    if (!player.id) {
        return <h3>Loading...</h3>
    }

    const leagueNodes = player.leagues.map((league) => {
        return <div key={league.id}>
            <Link to = {"/leagues/" + league.id}>
                {league.name}
            </Link>
            <p>Members: {league.players.length}</p>
            <p>Rank: {league.players.findIndex(leaguePlayer => leaguePlayer.id === player.id) + 1}</p>
        </div>
    })

    return (
        <>
            <h3>My Leagues</h3>
            {leagueNodes}
        </>
    )
}

export default Leagues;