import React, { useState } from 'react';

const JoinLeague = ({handleJoinLeague, toggleShowLeagueForm, showForm}) => {
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
        <div>
            <button className="btn btn-secondary m-3 d-grid gap-2 col-3 mx-auto fw-bold" id="join-league" onClick={toggleShowLeagueForm}>Join League</button>

            {showForm ? (
                <div className="container d-flex flex-wrap justify-content-center">

                <form className="card w-50" onSubmit={(event) => handleJoinLeague(joinCode, event)}>
                    <div className="card-header">
                        <h5 className="card-title">Join a League</h5>
                    </div>
                    <div className="card-body">
                        <input type="text"
                            name="join-code"
                            placeholder="Enter league code"
                            id="join_code"
                            value={joinCode.join_code}
                            onChange={handleJoinCodeChange}
                            ></input>
                    </div>
                    <div className="mb-3">
                        <button className="btn btn-primary" type="submit">Join League</button>
                    </div>
                </form>
                </div>
            ) : (
                null
            )}

        </div>
    )
}

export default JoinLeague;