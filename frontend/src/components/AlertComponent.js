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
            <div className="d-flex justify-content-between alert alert-info" role="alert" style={{position: 'fixed', 'z-index': 1, top: 15 + 'px', left: 50 + '%', transform: 'translateX(-50%)'}}>
                <span>{errorMessage}</span>
                <button type="button" className="btn-close ms-3" aria-label="Close" onClick={() => closeModal()}>
                    {/* <span aria-hidden="true">&times;</span> */}
                </button>
            </div>
            
        </div>
    )
} 

export default AlertComponent