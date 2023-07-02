import React from "react"; 
import { Link } from "react-router-dom";
import { ShoppingCart} from "phosphor-react";

export const Navbar = () => {
    return <div clasName="navbar">
        <div className="links">
            <Link to="/">Shop</Link>
            <Link to="/cart"> 
                <ShoppingCart size=" 30"/>
            </Link>

        </div>
    </div>
}