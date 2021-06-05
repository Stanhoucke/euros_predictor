import React, { useContext } from 'react';
import PlayerContext from '../utils/PlayerContext';

const PlayerGroup = ({group}) => {
    const player = useContext(PlayerContext)

    return (
        <div>
            <h4>Group {group.name}</h4>
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th>Country</th>
                        <th>MP</th>
                        <th>W</th>
                        <th>D</th>
                        <th>L</th>
                        <th>GF</th>
                        <th>GA</th>
                        <th>GD</th>
                        <th>Pts</th>
                    </tr>
                </thead>
                <tbody>
                {group.player_teams.map(team => {
                    return <tr key={team.id}>
                        <td>{team.group_info.rank}</td>
                        <td>{team.team.name}</td>
                        <td>{team.group_info.played}</td>
                        <td>{team.group_info.won}</td>
                        <td>{team.group_info.drawn}</td>
                        <td>{team.group_info.lost}</td>
                        <td>{team.group_info.for}</td>
                        <td>{team.group_info.against}</td>
                        <td>{team.group_info.difference}</td>
                        <td>{team.group_info.points}</td>
                    </tr>
                    })}
                </tbody>
            </table>
        </div>
    )
}

export default PlayerGroup;