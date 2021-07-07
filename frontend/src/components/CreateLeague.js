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
        <div>
            <button className="btn btn-secondary m-3 d-grid gap-2 col-3 mx-auto fw-bold" id="create-league" onClick={toggleShowLeagueForm}>Create League</button>

            { showForm ? (
                <div className="container d-flex flex-wrap justify-content-center">
                    <form className="card w-50" onSubmit={(event) => handleCreateLeague(leagueName, event)}>
                        <div className="card-header">
                            <h5 className="card-title">Create a League</h5>
                        </div>
                        <div className="card-body">
                            <input type="text"
                                name="league-name"
                                placeholder="Enter league name"
                                id="name"
                                value={leagueName.name}
                                onChange={handleNameChange}
                            ></input>
                        </div>
                        <div className="mb-3">
                            <button className="btn btn-primary" type="submit" >Create League</button>
                        </div>
                    </form>
                </div>
            ) : (
                null
            )}
        </div>
    )
}

export default CreateLeague;