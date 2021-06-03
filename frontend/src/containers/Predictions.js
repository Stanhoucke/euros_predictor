import React, { useContext, useEffect, useState } from 'react';
import PlayerGroup from '../components/PlayerGroup';
import PlayerPrediction from '../components/PlayerPrediction';
import PlayerContext from '../utils/PlayerContext';

const Predictions = () => {
    const [playerPredictions, setPlayerPredictions] = useState({});
    const player = useContext(PlayerContext)

    useEffect (() => {
        if (player.id) {
            setPredictedScores();
        }
    }, [player])
    
    if (!player.id) {
        return <h3>Loading...</h3>
    }

    const groupNodes = player.player_groups.map(group => {
        return <PlayerGroup key={group.id} group={group}/>
    })

    const setPredictedScores = () => {
        const scores = {}

        player.predictions.map(prediction => {
            scores[prediction.id] = {
                    home: prediction.goals.home,
                    away: prediction.goals.away
                }
        })
        setPlayerPredictions(scores);
    }

    const handleScoreChange = (prediction, event) => {
        const {id, value} = event.target
        setPlayerPredictions( existingDetails => ({
            ...existingDetails,
            [prediction.id]: { 
                ...existingDetails[prediction.id],
                [id]: parseInt(value)
            }
        }))
    }

    const predictionNodes = player.predictions.map(prediction => {
        return <PlayerPrediction key={prediction.id} prediction={prediction} handleScoreChange={handleScoreChange}/>
    })


    return (
        <>
            <h3>{player.first_name}'s Predictions</h3>
            <h3>Groups</h3>
            {groupNodes}
            <h3>Match Predictions</h3>
            {predictionNodes}
        </>
    )
}

export default Predictions;