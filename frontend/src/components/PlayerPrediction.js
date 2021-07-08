import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const PlayerPrediction = ({prediction, playerPredictions, handleScoreChange, disablePredictionInputs}) => {
    const player = useContext(PlayerContext)

    if (!playerPredictions) {
        return <div className="spinner-grow text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
        </div>
    }

    const formatMatchDate = () => {
        const date = prediction.match.date
        return date.substring(0, date.length - 7)
    }

    const matchDate = formatMatchDate();

    const getGroupName = () => {
        if (prediction.match.group_name) {
            return <span> - {prediction.match.group_name}</span>
        }
    }

    const groupName = getGroupName();

    return (
        <div className="card m-1 bg-light" style={{width: 25 + 'em'}}>
            <h4 className="mt-2 fs-6">{matchDate}</h4>
            <p className="mb-0 fs-6 fw-light">{prediction.match.location}{groupName}</p>
            <div>
                <span className="p-2">
                    {
                        prediction.match.team_1 ? 
                        prediction.match.team_1.name
                        :
                        "TBD"
                    }
                </span>
                <input className="m-2" style={{width: 2.5 + 'em'}} type="number" min="0"
                    id="home"
                    placeholder="0"
                    value={playerPredictions[prediction.id].home}
                    onChange={(event) => handleScoreChange(prediction, event)}
                    disabled={disablePredictionInputs}
                />
                    
                <span> - </span>
                <input className="m-2" style={{width: 2.5 + 'em'}} type="number" min="0"
                    id="away"
                    placeholder="0"
                    value={playerPredictions[prediction.id].away}
                    onChange={(event) => handleScoreChange(prediction, event)}
                    disabled={disablePredictionInputs}
                />
                <span className="p-2">
                    {
                        prediction.match.team_2 ? 
                        prediction.match.team_2.name
                        :
                        "TBD"
                    }
                </span>
            </div>
        </div>
    )
}

export default PlayerPrediction;