import React from 'react';

const Home = () => {
    return (
        <>
            <div className="row m-5 p-3 bg-info rounded-3">
                <h3 className="col-sm-4 display-2">Euro 2020 Predictor</h3>
                <span className="col-sm-8 lead d-flex align-items-center p-5">
                    Predict the outcome of each match of the Euro 2020 tournament - and crown your Euro 2020 champion!
                </span>
            </div>

            <div class="d-flex flex-row flex-wrap justify-content-around mb-5">
                <div class="p-4 m-3 card justify-content-center bg-secondary text-light" style={{width: 15 + 'em'}}>
                    Compete against all users and climb the Overall League table
                </div>
                <div class="p-4 m-3 card justify-content-center bg-secondary text-light" style={{width: 15 + 'em'}}>
                    Join and create private mini-leagues to play against your friends
                </div>
            </div>

            <div className="container mb-5">
                <h3>Scoring Points</h3>
                <ul className="list-group list-group-flush">
                    <li className="list-group-item p-4">
                        Score three points for correctly predicting the match outcome
                    </li>
                    <li className="list-group-item p-4">
                        Score an additional point for correctly predicting the number of goals scored by a team
                    </li>

                </ul>
            </div>
        </>
    )
}

export default Home;