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
                <h3 className="mb-4">{league.name}</h3>
                {league.name === "Overall" ? (
                    null
                ) : (
                    <h4 className="mb-5">Join Code: <span className="badge bg-dark user-select-all">{league.join_code}</span></h4>
                )}
            </div>
            
            <div className="container">
                <ul className="list-group">
                    <LeaguePlayer players={league.players}/>
                </ul>
            </div>
        </>
    )
}

export default LeagueDetails;