import React, { useState, useContext, useEffect } from "react";
import axios from "axios"
import { PRODUCTS } from "../../products";
import { ShopContext } from "../../context/shop-context";
import { CartItem } from "./cart-items"
import { useNavigate } from "react-router-dom";
import "./cart.css"

export const Cart = () => {
    const { cartItems, getTotalCartAmount } = useContext(ShopContext);
    const totalAmount = getTotalCartAmount();

    const navigate = useNavigate();


    const [products, setProducts] = useState([]);
    
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/produtos/").then((response) => {
                setProducts(response.data);
        });
    }, []);
    console.log(products);



    return <div className="cart">
        <div>
            <h1> Your Cart Items</h1>
        </div>
        <div className="cartItems">
            {products.map((product) => /* cartItems[product.id] > 0 && */ <CartItem data={product} />)}
        </div>

        {/* totalAmount > 0 ? (
            <div className="checkout">
                    <p> Subtotal: ${totalAmount}</p>
                    <button onClick={() => navigate("/")}> Continue Shopping</button>
                    <button> Checkout</button>
            </div>
        ) : (
            <h1> Your Cart is Empty</h1> 
        )*/}
    </div>
}