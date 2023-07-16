import { useState } from "react"
import axios from "axios";
import "./Register.css"
import { useNavigate } from "react-router-dom";

export const Register = () => {
    // State variables for capturing form input values
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [passwd, setPasswd] = useState("");

    // Access the navigation object for redirecting after registration
    const navigate = useNavigate();

    // Function to handle user registration
    const userRegister = () => {
        const newUser = {
            email: email,
            password: passwd,
            first_name: firstName,
            last_name: lastName
        }

        // Send a POST request to the server to register the user,
        // display a success message and redirect to the login page
        axios.post("http://127.0.0.1:8080/api/accounts/signup/", newUser).then((resp) => {
            alert(`Successful registration`);
            navigate("/login")
        }).catch((error) => alert("Erro in registration!"))
    }

    return (
        <div className="formulario">
            <h1>Register</h1>
            <p>Please fill in this form to create an account.</p>
            
            <label><b> First Name: </b></label> <br />
            <input 
                type="text" 
                placeholder="Type your first name" 
                onChange={(e) => setFirstName(e.target.value)} /> <br />
            <label><b> Last Name: </b></label> <br />
            <input 
                type="text" 
                placeholder="Type your last name" 
                onChange={(e) => setLastName(e.target.value)} /> <br />
            <label><b> Email: </b></label> <br />
            <input 
                type="text" 
                placeholder="Type your email" 
                onChange={(e) => setEmail(e.target.value)} /> <br />
            <label><b> Password: </b></label> <br />
            <input 
                type="password"
                placeholder="Type your password"
                onChange={(e) => setPasswd(e.target.value)} /> <br />
            <button onClick={userRegister}>Register</button>
        </div>
    )
}