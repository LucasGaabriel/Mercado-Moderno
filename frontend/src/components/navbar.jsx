import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { ShoppingCart } from "phosphor-react";
import "./navbar.css";
import { ShopContext } from "../context/shop-context";
import axios from "axios";

export const Navbar = () => {
  const { logged, setLogged } = useContext(ShopContext);

  const logout = () => {
    if( logged ) {
      axios.get("http://localhost:8080/api/accounts/logout/")
      .then((resp) => {
        alert("successfully logged out!")
        axios.defaults.headers.common['Authorization'] = null;
        localStorage.removeItem('token');
        sessionStorage.removeItem('token');
        setLogged(false);
      })
      .catch((error) => {
        console.log("Erro ao deslogar!");
      })
    }
  }
  return <div className="navbar">
      <div className="links">
        <Link to="/register"> Register </Link>
        <Link to="/login" onClick={logout}> {logged ? "Logout" : "Login"} </Link>
        <Link to="/"> Shop </Link>
        <Link to="/cart">
          <ShoppingCart size={32} />
        </Link>
      </div>
    </div>
};