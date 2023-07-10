import { React, useContext } from "react";
import { ShopContext } from "../../context/shop-context";
import { CartItem } from "./cart-items"
import { useNavigate } from "react-router-dom";
import "./cart.css"

export const Cart = () => {
    const { cartItems, products, checkout, getTotalCartAmount } = useContext(ShopContext);
    const navigate = useNavigate();

    let totalAmount = getTotalCartAmount();

    return <div className="cart">
        <div>
            <h1> Your Cart Items</h1>
        </div>
        <div className="cartItems">
            {products.map((product) => cartItems[product.id] > 0 && <CartItem data={product}/>)}
        </div>

        { totalAmount > 0 ? (
            <div className="checkout">
                    <p> Subtotal: ${Number(totalAmount).toFixed(2)}</p>
                    <button onClick={() => navigate("/")}> Continue Shopping</button>
                    <button onClick={checkout}> Checkout</button>
            </div>
        ) : (
            <h1> Your Cart is Empty </h1> 
        )}
    </div>
}