import React, { useContext, useEffect, useState } from 'react';
import PlayerGroup from '../components/PlayerGroup';
import PlayerPrediction from '../components/PlayerPrediction';
import PlayerThirdPlaceGroup from '../components/PlayerThirdPlaceGroup';
import PlayerContext from '../utils/PlayerContext';

const Predictions = ({setErrorMessage, handleSubmitPredictions}) => {
    const [playerPredictions, setPlayerPredictions] = useState({});
    const [disablePredictionInputs, setDisablePredictionInputs] = useState({
        group_matches: false,
        round_16: false,
        quarter_finals: false,
        semi_finals: false,
        final: false
    })
    const player = useContext(PlayerContext)

    useEffect (() => {
        if (player.id) {
            setPredictedScores();
            toggleDisablePredictionInputs();
        }
    }, [player])
    
    if (!player.id) {
        return <div className="d-flex flex-column align-items-center">
            <strong className="h3 mb-4 text-primary">Loading...</strong>
            <div className="spinner-border text-primary" role="status" aria-hidden="true" style={{width: '3em', height: '3em'}}></div>
        </div>
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

    const toggleDisablePredictionInputs = () => {
        const today = new Date()

        const groupMatchDeadline = new Date(player.predictions["1"][0].match.date)
        const round16Deadline = new Date(player.predictions["Round of 16"][0].match.date)
        const quarterFinalsDeadline = new Date(player.predictions["Quarter Finals"][0].match.date)
        const semiFinalsDeadline = new Date(player.predictions["Semi Finals"][0].match.date)
        const finalDeadline = new Date(player.predictions["Final"][0].match.date)

        if (today >= finalDeadline) {
            setDisablePredictionInputs({
                group_matches: true,
                round_16: true,
                quarter_finals: true,
                semi_finals: true,
                final: true
            })
        } else if (today >= semiFinalsDeadline) {
            setDisablePredictionInputs({
                group_matches: true,
                round_16: true,
                quarter_finals: true,
                semi_finals: true,
                final: false
            })
        } else if (today >= quarterFinalsDeadline) {
            setDisablePredictionInputs({
                group_matches: true,
                round_16: true,
                quarter_finals: true,
                semi_finals: false,
                final: false
            })
        } else if (today >= round16Deadline) {
            setDisablePredictionInputs({
                group_matches: true,
                round_16: true,
                quarter_finals: false,
                semi_finals: false,
                final: false
            })
        } else if (today >= groupMatchDeadline) {
            setDisablePredictionInputs(disabledDates => ({
                ...disabledDates,
                group_matches: true
            }))
        }
    }

    
    const groupNodes = player.player_groups.map(group => {
        return <PlayerGroup key={group.id} group={group}/>
    })

    const round1Matches = player.predictions["1"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <div key={prediction.id} className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange} disablePredictionInputs={disablePredictionInputs.group_matches}/>
    })
    const round2Matches = player.predictions["2"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <div key={prediction.id} className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange} disablePredictionInputs={disablePredictionInputs.group_matches}/>
    })
    const round3Matches = player.predictions["3"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <div key={prediction.id} className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange} disablePredictionInputs={disablePredictionInputs.group_matches}/>
    })
    const roundOf16Matches = player.predictions["Round of 16"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <div key={prediction.id} className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange} disablePredictionInputs={disablePredictionInputs.round_16}/>
    })
    const QuarterFinalMatches = player.predictions["Quarter Finals"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <div key={prediction.id} className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange} disablePredictionInputs={disablePredictionInputs.quarter_finals}/>
    })
    const SemiFinalMatches = player.predictions["Semi Finals"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <div key={prediction.id} className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange} disablePredictionInputs={disablePredictionInputs.semi_finals}/>
    })
    const FinalMatches = player.predictions["Final"].map(prediction => {
        if (!playerPredictions[prediction.id]){
            return <div key={prediction.id} className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        }
        return <PlayerPrediction key={prediction.id} prediction={prediction} playerPredictions={playerPredictions} handleScoreChange={handleScoreChange} disablePredictionInputs={disablePredictionInputs.final}/>
    })


    return (
        <>
            <h3>{player.first_name}'s Predictions</h3>
            
            <form className="mb-5" onSubmit={(event) => handleSubmitPredictions(playerPredictions, event)}>
                <h4 className="mt-4">Matchday 1</h4>
                <div className="container d-flex flex-wrap justify-content-center overflow-hidden">
                    {round1Matches}
                </div>
                <h4 className="mt-4">Matchday 2</h4>
                <div className="container d-flex flex-wrap justify-content-center overflow-hidden">
                    {round2Matches}
                </div>
                <h4 className="mt-4">Matchday 3</h4>
                <div className="container d-flex flex-wrap justify-content-center overflow-hidden">
                    {round3Matches}
                </div>
                <h4 className="mt-4">Round of 16</h4>
                <div className="container d-flex flex-wrap justify-content-center overflow-hidden">
                    {roundOf16Matches}
                </div>
                <h4 className="mt-4">Quarter Finals</h4>
                <div className="container d-flex flex-wrap justify-content-center overflow-hidden">
                    {QuarterFinalMatches}

                </div>
                <h4 className="mt-4">Semi Finals</h4>
                <div className="container d-flex flex-wrap justify-content-center overflow-hidden">
                    {SemiFinalMatches}
                </div>
                <h4 className="mt-4">Final</h4>
                <div className="container d-flex flex-wrap justify-content-center overflow-hidden">
                    {FinalMatches}
                </div>

                <div className="m-4">
                    <button className="btn btn-primary" type="submit">Save Predictions</button>
                </div>
            </form>

            <h3 className="mb-4">Groups</h3>
            <div className="container mb-5">
                <div className="row">
                    {groupNodes}
                    <PlayerThirdPlaceGroup/>
                </div>
            </div>

        </>
    )
}

export default Predictions;