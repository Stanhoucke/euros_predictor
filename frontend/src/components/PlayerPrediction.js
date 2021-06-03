import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';

const PlayerPrediction = ({prediction, handleScoreChange}) => {
    const [predictedScore, setPredictedScore] = useState({
        home: prediction.goals.home,
        away: prediction.goals.away,
        id: prediction.id
    })

    const player = useContext(PlayerContext)

    // const handleScoreChange = (event) => {
    //     const {id, value} = event.target
    //     setPredictedScore( existingDetails => ({
    //         ...existingDetails,
    //         [id]: parseInt(value)
    //     }))
    // }

    return (
        <div>
            <p>Match {prediction.id}</p>
            <span>{prediction.match.team_1.name}</span>
            <input type="number" min="0"
                id="home"
                placeholder="0"
                value={predictedScore.home}
                onChange={(event) => handleScoreChange(prediction, event)}
            />
                
            <span> - </span>
            <input type="number" min="0"
                id="away"
                placeholder="0"
                value={predictedScore.away}
                onChange={(event) => handleScoreChange(prediction, event)}
            />
            <span>{prediction.match.team_2.name}</span>
        </div>
    )
}

export default PlayerPrediction;