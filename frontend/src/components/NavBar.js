import React from 'react';
import { Link } from 'react-router-dom';
import Logout from './Logout';

const NavBar = ({token, handleLogout}) => {

    const authLinks = () => {
        if (token) {
            return <>
                <Link to={"/dashboard"} className="nav-link">Dashboard</Link>
                <Link to={"/predictions"} className="nav-link">Predictions</Link>
                <Link to={"/leagues"} className="nav-link">Leagues</Link>
                <Logout handleLogout={handleLogout}/>
            </>
        } else {
            return <>
                <Link to={"/login"} className="nav-link">Login</Link>
                <Link to={"/register"} className="nav-link">Register</Link>
            </>
        }
    } 
    

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-5 justify-content-center">
            <Link to={"/"} className="nav-link">Home</Link>
            {authLinks()}
        </nav>
    )
}

export default NavBar;