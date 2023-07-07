import { React, useContext, useState } from "react"
import { ShopContext } from "../../context/shop-context";

export const CartItem = (props) => {
    const { id, nome, preco, vendas, imagem, estoque } = props.data;
    const { cartItems, addToCart, removeFromCart, updateCartItemCount} = useContext(ShopContext);
    
    return <div className="cartItem">
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
}