import React from 'react';
import { Link } from 'react-router-dom';
import Logout from './Logout';

const NavBar = ({token, handleLogout}) => {

    const authLinks = () => {
        if (token) {
            return <>
                <Link to={"/dashboard"}>Dashboard</Link>
                <Logout handleLogout={handleLogout}/>
            </>
        } else {
            return <>
                <Link to={"/login"}>Login</Link>
                <Link to={"/register"}>Register</Link>
            </>
        }
    } 
    

    return (
        <>
            <Link to={"/"}>Home</Link>
            {authLinks()}
        </>
    )
}

export default NavBar;