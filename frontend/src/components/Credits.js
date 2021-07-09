import React from 'react';

const Credits = () => {
    return <>
        <div className="container bg-light p-5">
            <h1 className="display-1 mb-5">Euros 2020 Predictor</h1>
            <div className="d-flex justify-content-around">
                <h3 className="fw-normal"> Stanley Houcke</h3>
                <h3 className="fw-normal">Edinburgh, United Kingdom</h3>
            </div>
        </div>
        <div className="container bg-light ps-5 pe-5">
            <h3 className="border-top pt-5 pb-5">Technologies Used</h3>
            <div className="d-flex justify-content-around text-start">
                <div>
                    <h5><u>Backend</u></h5>
                    <ul>
                        <li>Python</li>
                        <li>Flask</li>
                        <li>PostgreSQL</li>
                        <li>api-football.com</li>
                    </ul>
                </div>
                <div>
                    <h5><u>Frontend</u></h5>
                    <ul>
                        <li>React js</li>
                        <li>Bootstrap</li>
                        <li>HTML</li>
                        <li>CSS</li>
                    </ul>
                </div>
            </div>
        </div>
    </>
}

export default Credits;