import { useState } from "react"
import "./Login.css"

export const Login = () => {
    const [email, setEmail] = useState("");
    const [passwd, setPasswd] = useState("");

    return <div className="formulario">
        <h1> Login </h1>
        <label> Email: </label> <br />
        <input 
            type="text" 
            placeholder="Type yout email" 
            onChange={(e) => setEmail(e.target.value)} /> <br />
        <label> Password: </label> <br />
        <input 
            type="password"
            placeholder="Type your password"
            onChange={(e) => setPasswd(e.target.value)} /> <br />
        <button>Login</button>
    </div>
}