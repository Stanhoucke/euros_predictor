import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const JoinLeague = ({handleJoinLeague, toggleShowLeagueForm, showForm}) => {
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
            <h3 id="join-league" onClick={toggleShowLeagueForm}>Join League</h3>

            {showForm ? (
                <form onSubmit={(event) => handleJoinLeague(joinCode, event)}>
                    <label htmlFor="join-code">Join a league: </label>
                    <input type="text"
                        name="join-code"
                        placeholder="Enter league code"
                        id="join_code"
                        value={joinCode.join_code}
                        onChange={handleJoinCodeChange}
                    ></input>
                    <button type="submit">Join League</button>
                </form>
            ) : (
                null
            )}
        </>
    )
}

export default JoinLeague;