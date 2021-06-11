import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const CreateLeague = ({handleCreateLeague, toggleShowLeagueForm, showForm}) => {
    const player = useContext(PlayerContext)

    const [leagueName, setLeagueName] = useState({
        name: ""
    })

    const handleNameChange = (event) => {
        const {id, value} = event.target
        setLeagueName({
            [id]: value
        })
    }

    return (
        <>
            <h3 id="create-league" onClick={toggleShowLeagueForm}>Create League</h3>

            { showForm ? (
                <form onSubmit={(event) => handleCreateLeague(leagueName, event)}>
                    <label htmlFor="league-name">Create a league: </label>
                    <input type="text"
                        name="league-name"
                        placeholder="Enter league name"
                        id="name"
                        value={leagueName.name}
                        onChange={handleNameChange}
                    ></input>
                    <button type="submit">Create League</button>
                </form>
            ) : (
                null
            )}
        </>
    )
}

export default CreateLeague;