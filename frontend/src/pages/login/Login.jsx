import { useState, useContext } from "react"
import { ShopContext } from "../../context/shop-context"
import axios from "axios"
import "./Login.css"
import { useNavigate } from "react-router-dom"

export const Login = () => {
    // State variables for store user email and password
    const [email, setEmail] = useState("");
    const [passwd, setPasswd] = useState("");

    // Accessing values from the ShopContext
    const { setLogged, setUserId } = useContext(ShopContext);

    // React Router hook for navigation
    const navigate = useNavigate()

    // Function to handle user login
    const userLogin = () => {
        const userData = {
            email: email,
            password: passwd
        };
    
        // Sending a POST request to the server with user data
        axios.post("http://127.0.0.1:8080/api/accounts/login/", userData)
        .then((resp) => {
            const token = resp.data.token;

            // Storing the token in the local storage
            localStorage.setItem('token', token);

            // Setting the authorization header for future requests
            axios.defaults.headers.common['Authorization'] = `Token ${token}`;

            axios.get(`http://localhost:8080/api/accounts/users/me/`)
            .then((res) => {
                let id = res.data.id;

                // Updating the state variables with user ID and login status
                setUserId(id);
                setLogged(true);
                
                alert(`Welcome, ${res.data.first_name}!`);

                // Navigating to the homepage
                navigate("/")
            })
            .catch((erro) => console.log(`Erro ao buscar dados de usuario com email ${email}`))
        })
        .catch((error) => alert(`ERRO: Credenciais incorretas ou login não cadastrado`));
    };

    return (
        <div className="formulario">
            <h1> Login </h1>
            <label><b> Email: </b></label> <br />
            <input 
                type="text" 
                placeholder="Type yout email" 
                onChange={(e) => setEmail(e.target.value)}
                /> <br />
            <label><b> Password: </b></label> <br />
            <input 
                type="password"
                placeholder="Type your password"
                onChange={(e) => setPasswd(e.target.value)} 
            /> <br />
            <button onClick={userLogin}>Login</button>
        </div>
    )
}