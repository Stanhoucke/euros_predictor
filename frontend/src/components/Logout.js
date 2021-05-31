import React from 'react';
import { Link } from 'react-router-dom';
import Request from '../helpers/Request';

const Logout = ({handleLogout}) => {

    const request = new Request();

    return (
        <Link to={"/login"} onClick={handleLogout}>Logout</Link>
    )
}

export default Logout;