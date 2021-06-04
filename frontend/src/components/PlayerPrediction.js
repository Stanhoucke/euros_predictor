import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const PlayerPrediction = ({prediction, playerPredictions, handleScoreChange}) => {
    const player = useContext(PlayerContext)

    if (!playerPredictions) {
        return <h3>Loading...</h3>
    }

    return (
        <div>
            <p>Match {prediction.id}</p>
            <span>{prediction.match.team_1.name}</span>
            <input type="number" min="0"
                id="home"
                placeholder="0"
                value={playerPredictions[prediction.id].home}
                onChange={(event) => handleScoreChange(prediction, event)}
            />
                
            <span> - </span>
            <input type="number" min="0"
                id="away"
                placeholder="0"
                value={playerPredictions[prediction.id].away}
                onChange={(event) => handleScoreChange(prediction, event)}
            />
            <span>{prediction.match.team_2.name}</span>
        </div>
    )
}

export default PlayerPrediction;