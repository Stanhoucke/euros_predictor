import React, { useContext } from 'react';
import PlayerContext from '../utils/PlayerContext';

const Predictions = () => {
    const player = useContext(PlayerContext)

    const groupNodes = player.player_groups.map(group => {
        return <div key={group.id}>
            <h4>Group {group.name}</h4>
            {group.player_teams.map(team => {
                return <div key={team.id}>
                    <span>{team.team.name}</span>
                    <span> {team.group_info.points}</span>
                </div>
            })}
        </div>
    })

    const predictionNodes = player.predictions.map(prediction => {
        return <div key={prediction.id}>
            <p>Match {prediction.id}</p>
            <span>{prediction.match.team_1.name}</span>
            <input type="number">{prediction.goals.home}</input>
            <span> - </span>
            <input type="number">{prediction.goals.away}</input>
            <span>{prediction.match.team_2.name}</span>
        </div>
    })

    if (!player) {
        return <h3>Loading...</h3>
    }

    return (
        <>
            <h3>{player.first_name}'s Predictions</h3>
            {groupNodes}
            {predictionNodes}
        </>
    )
}

export default Predictions;