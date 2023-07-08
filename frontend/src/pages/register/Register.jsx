import { useState } from "react"
import "./Register.css"

export const Register = () => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [passwd, setPasswd] = useState("");

    return <div className="formulario">
        <h1>Register</h1>
        <label> First Name: </label> <br />
        <input 
            type="text" 
            placeholder="Type your fisrt name" 
            onChange={(e) => setFirstName(e.target.value)} /> <br />
        <label> Last Name: </label> <br />
        <input 
            type="text" 
            placeholder="Type your last name" 
            onChange={(e) => setLastName(e.target.value)} /> <br />
        <label> Email: </label> <br />
        <input 
            type="text" 
            placeholder="Type your email" 
            onChange={(e) => setEmail(e.target.value)} /> <br />
        <label> Password: </label> <br />
        <input 
            type="password"
            placeholder="Type your password"
            onChange={(e) => setPasswd(e.target.value)} /> <br />
        <button>Register</button>
    </div>
}