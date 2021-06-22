import React, { useContext, useState } from 'react';
import PlayerContext from '../utils/PlayerContext';
import PlayerGroup from './PlayerGroup';
import cloneDeep from 'lodash/cloneDeep';

const PlayerThirdPlaceGroup = () => {
    const player = useContext(PlayerContext)
    
    const getThirdPlaceGroup = () => {
        const groups = player.player_groups;
        const thirdPlaceGroup = {
            name: "for Third Placed Teams",
            player_teams: []
        };
        
        thirdPlaceGroup.player_teams = groups.map(group => {
            return cloneDeep(group.player_teams[2]);
        })

        sortTeams(thirdPlaceGroup);
        rankTeams(thirdPlaceGroup.player_teams);

        return thirdPlaceGroup;
    }

    const sortTeams = (group) => {
        group.player_teams.sort(function(a, b) {
            if (a.group_info.difference === b.group_info.difference && a.group_info.points === b.group_info.points) {
                return b.group_info.for - a.group_info.for;
            } else if (a.group_info.points === b.group_info.points) {
                return b.group_info.difference - a.group_info.difference;
            } else {
                return b.group_info.points - a.group_info.points;
            }
        })
    }

    const rankTeams = (teams) => {
        for (let i = 0; i < teams.length; i++) {
            teams[i].group_info.rank = i + 1;
        }
        return teams;
    }
    
    const [thirdPlaceGroup, setThirdPlaceGroup] = useState(getThirdPlaceGroup())
    
    return (
        <>
            <PlayerGroup group={thirdPlaceGroup}/>
        </>
    )
}

export default PlayerThirdPlaceGroup;