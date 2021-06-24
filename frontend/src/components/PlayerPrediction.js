import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const PlayerPrediction = ({prediction, playerPredictions, handleScoreChange, disablePredictionInputs}) => {
    const player = useContext(PlayerContext)

    if (!playerPredictions) {
        return <h3>Loading...</h3>
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
        <div className="card ">
            <h4 className="card-title">{matchDate}</h4>
            <p className="card-subtitle">{prediction.match.location}{groupName}</p>
            <div>
                <span>
                    {
                        prediction.match.team_1 ? 
                        prediction.match.team_1.name
                        :
                        "TBD"
                    }
                </span>
                <input style={{width: 2.5 + 'em'}} type="number" min="0"
                    id="home"
                    placeholder="0"
                    value={playerPredictions[prediction.id].home}
                    onChange={(event) => handleScoreChange(prediction, event)}
                    disabled={disablePredictionInputs}
                />
                    
                <span> - </span>
                <input style={{width: 2.5 + 'em'}} type="number" min="0"
                    id="away"
                    placeholder="0"
                    value={playerPredictions[prediction.id].away}
                    onChange={(event) => handleScoreChange(prediction, event)}
                    disabled={disablePredictionInputs}
                />
                <span>
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