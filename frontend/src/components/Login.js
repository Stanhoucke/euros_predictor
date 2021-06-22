import React, { useState } from 'react';
import { useHistory } from 'react-router';
import Request from '../helpers/Request';

const Login = ({setErrorMessage, setToken}) => {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    let history = useHistory();
    
    const request = new Request();

    const loginUser = async (credentials) => {
       return request.post("http://localhost:5000/api/login", credentials)
    }

    const handleSubmit = async (event) => {
        event.preventDefault();

        const credentials = {
            "email": username,
            "password": password
        }

        const auth_token = await loginUser(credentials);
        if (auth_token?.auth_token){
            setToken(auth_token.auth_token)
            history.push("/dashboard")
        } else {
            setErrorMessage(auth_token.message)
        }
    }

    return (
        <>
        <div className="d-flex justify-content-center">
            <div className="card text-start w-50 mb-5">
                <div className="card-header text-center">
                    <h3>Please Log In</h3>
                </div>
            <form className="card-body" onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="email-login" className="form-label">Email address</label>
                    <input type="email" className="form-control" id="email-login" aria-describedby="emailHelp" onChange={e => setUsername(e.target.value)}/>
                </div>
                
                <div className="mb-3">
                    <label htmlFor="password-login" className="form-label">Password</label>
                    <input type="password" className="form-control" id="password-login" onChange={e => setPassword(e.target.value)}/>

                </div>

                <div className="mb-3 text-center">
                    <button type="submit" className="btn btn-primary">Login</button>
                </div>

            </form>
            </div>
            </div>
        </>
    )
}

export default Login;