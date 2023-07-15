import { React, useContext } from "react"
import { ShopContext } from "../../context/shop-context";

// Each item on the cart page
export const CartItem = (props) => {
    // Accessing values from the ShopContext
    const { cartItems, addToCart, removeFromCart, updateCartItemCount} = useContext(ShopContext);
    const { id, nome, preco, imagem } = props.data;
    
    return (
        <div className="cartItem">
            <img src={imagem} />
            <div className="description">
                <p><b>{nome}</b></p>
                <p> Price: ${preco}</p>
                <div className="countHandler">
                    <button onClick={() => removeFromCart(id)}> - </button>
                    <input value={cartItems[id]} onChange={(e) => updateCartItemCount(e.target.value, id)} type="number"/>
                    <button onClick={() => addToCart(id)}> + </button>
                </div>
            </div>
        </div>
    )
}