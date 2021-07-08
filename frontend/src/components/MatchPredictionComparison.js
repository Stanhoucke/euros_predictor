import React from 'react';

const MatchPredictionComparison = ({match, title}) => {
    if (!match.match) {
        return <div className="spinner-grow text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
        </div>
    }

    return (
        <div className="col">
            <h4>{title}</h4>

            <table className="table table-borderless table-light table-sm">
            <caption className="caption-top ">{match.match.date.substring(0, match.match.date.length - 7)}</caption>
                <thead className="table-light">
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
                        <td>v</td>
                        <td></td>
                        <td></td>
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
        </div>
    )
}

export default MatchPredictionComparison;