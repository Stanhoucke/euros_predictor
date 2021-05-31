import React, { useState } from 'react';
import { useHistory } from 'react-router';
import Request from '../helpers/Request';

const Register = ({setErrorMessage, setToken}) => {
    const [newUser, setNewUser] = useState({
        email: "",
        password: "",
        confirmPassword: "",
        firstName: "",
        lastName: "",
        teamName: ""
    });

    let history = useHistory();
    
    const request = new Request();

    const hasEmptyFields = () => {
        if (Object.values(newUser).includes("")) {
            setErrorMessage("All fields must be filled in.")
            return true;
        } else {
            return false;
        }
    }

    const checkPassword = () => {
        debugger;
        let validPassword = false;
        if (newUser.password.length < 8) {
            setErrorMessage("Password must be at least 8 characters.")
        } else if (newUser.password !== newUser.confirmPassword) {
            setErrorMessage("Passwords do not match.")
        } else {
            validPassword = true;
        }
        console.log(validPassword)
        return validPassword;
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        if (!hasEmptyFields() && checkPassword()) {
            request.post("http://localhost:5000/api/register", newUser)
            .then((res) => {
                if (res.status === "success"){
                    setToken(res.auth_token)
                    history.push("/dashboard")
                }
                setErrorMessage(res.message)
            })
        }
    }

    const handleInputChange = (event) => {
        const {id, value} = event.target
        setNewUser( existingDetails => ({
            ...existingDetails,
            [id]: value
        }))
    }

    return (
        <>
            <h3>Please Log In</h3>
            <form onSubmit={handleSubmit}>
                <label>
                    <p>Email</p>
                    <input type="email" required
                        id="email"
                        placeholder="Enter email"
                        value={newUser.email}
                        onChange={handleInputChange}
                    />
                    <small>This will also be your username.</small>
                </label>
                <label>
                    <p>Password</p>
                    <input type="password" required
                        id="password"
                        placeholder="Enter password"
                        value={newUser.password}
                        onChange={handleInputChange}
                    />
                </label>
                <label>
                    <p>Confirm Password</p>
                    <input type="password" required
                        id="confirmPassword"
                        placeholder="Confirm password"
                        value={newUser.confirmPassword}
                        onChange={handleInputChange}
                    />
                </label>
                <label>
                    <p>First Name</p>
                    <input type="text" required
                        id="firstName"
                        placeholder="Enter first name"
                        value={newUser.firstName}
                        onChange={handleInputChange}
                    />
                </label>
                <label>
                    <p>Last Name</p>
                    <input type="text" required
                        id="lastName"
                        placeholder="Enter last name"
                        value={newUser.lastName}
                        onChange={handleInputChange}
                    />
                </label>
                <label>
                    <p>Team Name</p>
                    <input type="text" required
                        id="teamName"
                        placeholder="Enter team name"
                        value={newUser.teamName}
                        onChange={handleInputChange}
                    />
                    <small>You can change this later.</small>
                </label>
                <div>
                    <button type="submit">Submit</button>
                </div>
            </form>
        </>
    )
}

export default Register;