import { React, useContext } from "react";
import { ShopContext } from "../../context/shop-context"; 

export const Product = (props) => {
    const { id, nome, preco, vendas, imagem, estoque } = props.data;
    const { cartItems, addToCart } = useContext(ShopContext);

    return <div className="product">
        <img src={imagem}/>
        <div className="description">
            <p>
                <b>{nome}</b>
            </p>
            <p>${preco}</p>
        </div>
        <button className="addToCartBtn" onClick={() => addToCart(id)}>
            Add To Cart {<> ({cartItems[id]}/{estoque}/{vendas})</>}
        </button>
    </div>
}