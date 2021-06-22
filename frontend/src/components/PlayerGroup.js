import React, { useContext } from 'react';
import PlayerContext from '../utils/PlayerContext';

const PlayerGroup = ({group}) => {
    const player = useContext(PlayerContext)

    return (
        <div className="col">
            <h4>Group {group.name}</h4>
            <table className="table table-striped">
                <thead className="table-primary">
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">Country</th>
                        <th scope="col">MP</th>
                        <th scope="col">W</th>
                        <th scope="col">D</th>
                        <th scope="col">L</th>
                        <th scope="col">GF</th>
                        <th scope="col">GA</th>
                        <th scope="col">GD</th>
                        <th scope="col">Pts</th>
                    </tr>
                </thead>
                <tbody>
                {group.player_teams.map(team => {
                    return <tr key={team.id}>
                        <th scope="row">{team.group_info.rank}</th>
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