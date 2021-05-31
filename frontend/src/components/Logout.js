import React from 'react';
import { Link } from 'react-router-dom';

const Logout = ({handleLogout}) => {

    return (
        <Link to={"/login"} onClick={handleLogout}>Logout</Link>
    )
}

export default Logout;