import React, { useContext, useEffect, useState } from 'react';
import { useParams } from 'react-router';
import PlayerContext from '../utils/PlayerContext';
import LeaguePlayer from './LeaguePlayer';

const LeagueDetails = ({findLeagueById}) => {
    let {id} = useParams();
    const player = useContext(PlayerContext)

    const [league, setLeague] = useState(findLeagueById(id))
    
    useEffect (() => {
        setLeague(findLeagueById(id))
    }, [player])

    if (!league) {
        return <h3>Loading...</h3>
    }


    return (
        <>
            <div key={league.id}>
                <h3>{league.name}</h3>
                <p>Join Code: {league.join_code}</p>
                <LeaguePlayer players={league.players}/>
            </div>
        </>
    )
}

export default LeagueDetails;