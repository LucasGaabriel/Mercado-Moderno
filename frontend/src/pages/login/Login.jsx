import { useState, useContext } from "react"
import { ShopContext } from "../../context/shop-context"
import axios from "axios"
import "./Login.css"

export const Login = () => {
    const [email, setEmail] = useState("");
    const [passwd, setPasswd] = useState("");
    const {logged, setLogged, setUserId} = useContext(ShopContext);

    const userLogin = () => {
        const userData = {
            email: email,
            password: passwd
        };
    
        axios.post("http://127.0.0.1:8080/api/accounts/login/", userData)
        .then((resp) => {
            const token = resp.data.token;
            localStorage.setItem('token', token);
            axios.defaults.headers.common['Authorization'] = `Token ${token}`;

            axios.get(`http://localhost:8080/api/accounts/users/me/`)
            .then((res) => {
                let id = res.data.id;
                setUserId(id);
                setLogged(true);
                console.log(res);
            })
            .catch((erro) => console.log(`Erro ao buscar dados de usuario com email ${email}`))
        })
        .catch((error) => alert(`ERRO: Credenciais incorretas ou login não cadastrado`));
    };

    return <div className="formulario">
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
}