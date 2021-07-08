import React, { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import Logout from './Logout';

const NavBar = ({token, handleLogout}) => {
    const [navLinkClass, setNavLinkClass] = useState({
        "/": "nav-link active",
        "/login": "nav-link",
        "/register": "nav-link",
        "/dashboard": "nav-link",
        "/predictions": "nav-link",
        "/leagues": "nav-link"
    })

    const location = useLocation();

    useEffect(() => {
        toggleActivePage();
    }, [location])

    const toggleActivePage = () => {
        const activePage = window.location.pathname;

        const navLinkClasses = {
            "/": "nav-link",
            "/login": "nav-link",
            "/register": "nav-link",
            "/dashboard": "nav-link",
            "/predictions": "nav-link",
            "/leagues": "nav-link"
        }

        if (activePage.includes("leagues")){
            navLinkClasses["/leagues"] = "nav-link active"
        } else {
            navLinkClasses[activePage] = "nav-link active"
        }
        
        setNavLinkClass(navLinkClasses);
    }

    const authLinks = () => {
        if (token) {
            return <>
                <Link to={"/dashboard"} className={navLinkClass["/dashboard"]}>Dashboard</Link>
                <Link to={"/predictions"} className={navLinkClass["/predictions"]}>Predictions</Link>
                <Link to={"/leagues"} className={navLinkClass["/leagues"]}>Leagues</Link>
                <Logout handleLogout={handleLogout}/>
            </>
        } else {
            return <>
                <Link to={"/login"} className={navLinkClass["/login"]}>Login</Link>
                <Link to={"/register"} className={navLinkClass["/register"]}>Register</Link>
            </>
        }
    } 
    
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4 justify-content-center nav-pills">
            <div className="container-fluid">
                <Link to={"/"} className="navbar-brand">Euro 2020 Predictor</Link>
            </div>
            <Link to={"/"} id="home" className={navLinkClass["/"]}>Home</Link>
            {authLinks()}
        </nav>
    )
}

export default NavBar;