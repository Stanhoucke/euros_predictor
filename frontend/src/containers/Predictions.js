import React, { useContext, useEffect, useState } from 'react';
import PlayerGroup from '../components/PlayerGroup';
import PlayerPrediction from '../components/PlayerPrediction';
import PlayerContext from '../utils/PlayerContext';

const Predictions = ({setErrorMessage, handleSubmitPredictions}) => {
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

    const setPredictedScores = () => {
        const scores = {}
        for (const [round_name, round_value] of Object.entries(player.predictions)) {
            round_value.map(prediction => {
                scores[prediction.id] = {
                        home: prediction.goals.home,
                        away: prediction.goals.away
                    }
            })
            setPlayerPredictions(scores);
        }
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

    
    const groupNodes = player.player_groups.map(group => {
        return <PlayerGroup key={group.id} group={group}/>
    })

    const round1Matches = player.predictions["1"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <h3 key={prediction.id}>Loading...</h3>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange}/>
    })
    const round2Matches = player.predictions["2"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <h3 key={prediction.id}>Loading...</h3>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange}/>
    })
    const round3Matches = player.predictions["3"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <h3 key={prediction.id}>Loading...</h3>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange}/>
    })
    const roundOf16Matches = player.predictions["Round of 16"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <h3 key={prediction.id}>Loading...</h3>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange}/>
    })
    const QuarterFinalMatches = player.predictions["Quarter Finals"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <h3 key={prediction.id}>Loading...</h3>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange}/>
    })
    const SemiFinalMatches = player.predictions["Semi Finals"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <h3 key={prediction.id}>Loading...</h3>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange}/>
    })
    const FinalMatches = player.predictions["Final"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <h3 key={prediction.id}>Loading...</h3>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange}/>
    })


    return (
        <>
            <h3>{player.first_name}'s Predictions</h3>
            <h3>Groups</h3>
            {groupNodes}
            <h3>Match Predictions</h3>
            <form onSubmit={(event) => handleSubmitPredictions(playerPredictions, event)}>
                <p>Matchday 1</p>
                {round1Matches}
                <p>Matchday 2</p>
                {round2Matches}
                <p>Matchday 3</p>
                {round3Matches}
                <p>Round of 16</p>
                {roundOf16Matches}
                <p>Quarter Finals</p>
                {QuarterFinalMatches}
                <p>Semi Finals</p>
                {SemiFinalMatches}
                <p>Final</p>
                {FinalMatches}

                <button type="submit">Save Predictions</button>
                <small>You can change these later</small>
            </form>
        </>
    )
}

export default Predictions;