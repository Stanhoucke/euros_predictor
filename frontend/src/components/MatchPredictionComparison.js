import React from 'react';

const MatchPredictionComparison = ({match, title}) => {
    return (
        <>
            <h4>{title}</h4>
            <p>{match.match.date.substring(0, match.match.date.length - 7)}</p>

            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th>Prediction</th>
                        <th>Result</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{match.match.team_1.name}</td>
                        <td>{match.goals.home}</td>
                        <td>
                            {
                                match.match.goals.home !== null ?
                                match.match.goals.home 
                                :
                                "-"
                            }
                        </td>
                    </tr>
                    <tr>
                        <td>{match.match.team_2.name}</td>
                        <td>{match.goals.away}</td>
                        <td>
                            {
                                match.match.goals.away !== null ?
                                match.match.goals.away
                                :
                                "-"
                            }
                        </td>
                    </tr>
                </tbody>
            </table>


        </>
    )
}

export default MatchPredictionComparison;