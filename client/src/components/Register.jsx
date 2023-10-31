import React from "react";

export const Register = (props) => {

    function submit(e){
        e.preventDefault()
        console.log('IT WORKS')
    }

    return (
        <div>
            <div className="input">
                <input type="text"/>
            </div>
            <div className="input">
                <input type="email"/>
            </div>
            <div className="input">
                <input type="password"/>
            </div>
            <div className="input">
                <input type="password"/>
            </div>
            <a href={'#'} className="button" onClick={(e) => submit(e)}>Submit</a>
        </div>
    )
}