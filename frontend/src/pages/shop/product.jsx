import { React, useContext } from "react";
import { ShopContext } from "../../context/shop-context"; 

// Each item on the shop page
export const Product = (props) => {
    // Accessing values from the ShopContext
    const { id, nome, preco, imagem} = props.data;
    const { cartItems, addToCart } = useContext(ShopContext);

    return (
        <div className="product">
            <img src={imagem}/>
            <div className="description">
                <p>
                    <b>{nome}</b>
                </p>
                <p>${preco}</p>
            </div>
            <button className="addToCartBtn" onClick={() => addToCart(id)}>
                Add To Cart {cartItems[id] > 0 && <> ({cartItems[id]})</>}
            </button>
        </div>
    )
}