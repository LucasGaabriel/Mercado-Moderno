import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { ShoppingCart } from "phosphor-react";
import "./navbar.css";
import { ShopContext } from "../context/shop-context";
import axios from "axios";

/**
 * The navbar component, it's shown by all pages
 * @returns The html code to render the navbar
 */
export const Navbar = () => {
  const { logged, setLogged } = useContext(ShopContext);

  /**
   * If user logged take off the
   * user token and set logged to 'false'
   */
  const logout = () => {
    if( logged ) {
      axios.get("http://localhost:8080/api/accounts/logout/")
      .then((resp) => {
        alert("successfully logged out!")

        // Resetting the authorization header
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

  /**
   * The html code to show the navigation bar
   */
  return (
    <div className="navbar">
      <div className="links">
        <Link to="/register"> Register </Link>
        {/* 'Login' text turn to 'Logout' when logged */}
        <Link to="/login" onClick={logout}> {logged ? "Logout" : "Login"} </Link> 
        <Link to="/"> Shop </Link>
        <Link to="/cart">
          <ShoppingCart size={32} />
        </Link>
      </div>
    </div>
  )
};