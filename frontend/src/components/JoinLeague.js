import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const JoinLeague = ({handleJoinLeague}) => {
    const player = useContext(PlayerContext)

    const [joinCode, setJoinCode] = useState({
        join_code: ""
    })

    const handleJoinCodeChange = (event) => {
        const {id, value} = event.target
        setJoinCode({
            [id]: value
        })
    }

    return (
        <>
            <h3>Join League</h3>
            <form onSubmit={(event) => handleJoinLeague(joinCode, event)}>
                <label htmlFor="join-league">Join a league: </label>
                <input type="text"
                    name="join-league"
                    placeholder="Enter league code"
                    id="join_code"
                    value={joinCode.join_code}
                    onChange={handleJoinCodeChange}
                ></input>
                <button type="submit">Join League</button>
            </form>
        </>
    )
}

export default JoinLeague;