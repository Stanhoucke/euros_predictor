import React, { useState } from 'react';
import { useHistory } from 'react-router';
import Request from '../helpers/Request';

const Login = ({setErrorMessage, setToken, token}) => {
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
            <h3>Please Log In</h3>
            <form onSubmit={handleSubmit}>
                <label>
                    <p>Username</p>
                    <input type="email" onChange={e => setUsername(e.target.value)}/>
                </label>
                <label>
                    <p>Password</p>
                    <input type="password" onChange={e => setPassword(e.target.value)}/>
                </label>
                <div>
                    <button type="submit">Submit</button>
                </div>
            </form>
            {token}
        </>
    )
}

export default Login;