import React, { useState, useEffect } from 'react';

const AlertComponent = ({errorMessage, setErrorMessage}) => {
    const [modalDisplay, setModalDisplay] = useState('none');
    const openModal = () => {
        setModalDisplay('block');     
    }
    const closeModal = () => {
        setModalDisplay('none'); 
        setErrorMessage(null);
    }
    useEffect(() => {
        if(errorMessage !== null) {
            openModal()
        } else {
            closeModal()
        }
    });
    
    return(
        <div 
            className="alert"
            role="alert" 
            id="alertPopUp"
            style={{ display: modalDisplay }}
        >
            <div className="d-flex alertMessage">
                <span>{errorMessage}</span>
                <button type="button" className="close" aria-label="Close" onClick={() => closeModal()}>
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            
        </div>
    )
} 

export default AlertComponent