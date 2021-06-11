import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const CreateLeague = ({handleCreateLeague}) => {
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
            <h3>Create League</h3>
            <form onSubmit={(event) => handleCreateLeague(leagueName, event)}>
                <label htmlFor="create-league">Create a league: </label>
                <input type="text"
                    name="create-league"
                    placeholder="Enter league name"
                    id="name"
                    value={leagueName.name}
                    onChange={handleNameChange}
                ></input>
                <button type="submit">Create League</button>
            </form>
        </>
    )
}

export default CreateLeague;