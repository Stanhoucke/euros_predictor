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
        let validPassword = false;
        if (newUser.password.length < 8) {
            setErrorMessage("Password must be at least 8 characters.")
        } else if (newUser.password !== newUser.confirmPassword) {
            setErrorMessage("Passwords do not match.")
        } else {
            validPassword = true;
        }
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
        <div className="d-flex justify-content-center">
            <div className="card text-start w-50 mb-5">
                <div className="card-header text-center">
                    <h3>Please Register</h3>
                </div>

                <form className="card-body" onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="email" className="form-label">Email</label>
                        <input className="form-control" type="email" required
                            id="email"
                            placeholder="Enter email"
                            value={newUser.email}
                            onChange={handleInputChange}
                        />
                        <small id="emailHelp" class="form-text">We'll never share your email with anyone else.</small>
                    </div>
                    <div className="mb-3">
                    <label htmlFor="password" className="form-label">Password</label>
                            <input className="form-control" type="password" required
                                id="password"
                                placeholder="Enter password"
                                value={newUser.password}
                                onChange={handleInputChange}
                            />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="confirmPassword" className="form-label">Confirm password</label>
                        <input className="form-control" type="password" required
                            id="confirmPassword"
                            placeholder="Confirm password"
                            value={newUser.confirmPassword}
                            onChange={handleInputChange}
                        /> 
                    </div>
                    <div className="mb-3">
                        <label htmlFor="firstName" className="form-label">First name</label>
                            <input className="form-control" type="text" required
                                id="firstName"
                                placeholder="Enter first name"
                                value={newUser.firstName}
                                onChange={handleInputChange}
                            />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="lastName" className="form-label">Last name</label>
                            <input className="form-control" type="text" required
                                id="lastName"
                                placeholder="Enter last name"
                                value={newUser.lastName}
                                onChange={handleInputChange}
                            />

                    </div>
                    <div className="mb-3">
                        <label htmlFor="teamName" className="form-label">Team name</label>
                            <input className="form-control" type="text" required
                                id="teamName"
                                placeholder="Enter team name"
                                value={newUser.teamName}
                                onChange={handleInputChange}
                            />
                            <small className="form-text">You can change this later.</small>

                    </div>
                    <div className="mb-3 text-center">
                        <button type="submit" className="btn btn-primary">Register</button>
                    </div>
                </form>

            </div>
        </div>
    )
}

export default Register;