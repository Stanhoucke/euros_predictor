import React, { useContext, useEffect, useState } from 'react';
import PlayerGroup from '../components/PlayerGroup';
import PlayerPrediction from '../components/PlayerPrediction';
import Request from '../helpers/Request';
import PlayerContext from '../utils/PlayerContext';

const Predictions = ({setErrorMessage}) => {
    const [playerPredictions, setPlayerPredictions] = useState({});
    const player = useContext(PlayerContext)

    const request = new Request();

    useEffect (() => {
        if (player.id) {
            setPredictedScores();
        }
    }, [player])
    
    if (!player.id) {
        return <h3>Loading...</h3>
    }

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

    const handleSubmitPredictions = (event) => {
        event.preventDefault();
        
        request.authPost("http://localhost:5000/api/predictions", playerPredictions, localStorage.getItem("auth_token"))
        .then((res) => {
            setErrorMessage(res.message)
        })
    }

    const groupNodes = player.player_groups.map(group => {
        return <PlayerGroup key={group.id} group={group}/>
    })

    const predictionNodes = player.predictions.map(prediction => {
        return <PlayerPrediction key={prediction.id} prediction={prediction} handleScoreChange={handleScoreChange}/>
    })


    return (
        <>
            <h3>{player.first_name}'s Predictions</h3>
            <h3>Groups</h3>
            {groupNodes}
            <h3>Match Predictions</h3>
            <form onSubmit={handleSubmitPredictions}>
                {predictionNodes}
                <button type="submit">Save Predictions</button>
                <small>You can change these later</small>
            </form>
        </>
    )
}

export default Predictions;