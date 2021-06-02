import React, { useState } from 'react';

export default function useToken() {
    const getToken = () => {
        const userToken = localStorage.getItem("auth_token")
        return userToken
    }

    const [token, setToken] = useState(getToken());

    const saveToken = (auth_token) => {
        localStorage.setItem("auth_token", auth_token)
        setToken(auth_token)
    }

    return {
        setToken: saveToken,
        token
    }

}