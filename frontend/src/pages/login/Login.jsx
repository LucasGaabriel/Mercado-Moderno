import { useState } from "react"
import axios from "axios"
import "./Login.css"

export const Login = () => {
    const [email, setEmail] = useState("");
    const [passwd, setPasswd] = useState("");

    const userLogin = () => {
        const userData = {
            email: email,
            password: passwd
        };
    
        console.log(userData);
    
        axios.post("http://127.0.0.1:8080/api/accounts/login/", userData)
            .then((resp) => {
                console.log(resp);
    
                const token = resp.data.token;
    
                localStorage.setItem('token', token);
    
                axios.defaults.headers.common['Authorization'] = `Token ${token}`;

                getUserData()


            })
            .catch((error) => console.log(error));
    };
    
    
    const getUserData = () => {
        axios.get('http://localhost:8080/api/accounts/users/me/')
        .then((res) => {
            console.log(res.data.id);
            axios.get(`http://localhost:8080/api/carrinhos/${res.data.id}/produtos/`)
            .then((res) => {
                console.log(res);
            })
        })
        .catch((error) => {
            console.error(error);
        });
    };
    

    return <div className="formulario">
        <h1> Login </h1>
        <label> Email: </label> <br />
        <input 
            type="text" 
            placeholder="Type yout email" 
            onChange={(e) => setEmail(e.target.value)}
            /> <br />
        <label> Password: </label> <br />
        <input 
            type="password"
            placeholder="Type your password"
            onChange={(e) => setPasswd(e.target.value)} 
        /> <br />
        <button onClick={userLogin}>Login</button>
    </div>
}