import React, { useContext } from 'react';
import PlayerContext from '../utils/PlayerContext';

const PlayerGroup = ({group}) => {
    const player = useContext(PlayerContext)

    return (
        <div>
            <h4>Group {group.name}</h4>
            {group.player_teams.map(team => {
                return <div key={team.id}>
                    <span>{team.team.name}</span>
                    <span> {team.group_info.points}</span>
                </div>
            })}
        </div>
    )
}

export default PlayerGroup;