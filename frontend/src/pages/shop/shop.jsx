import { React, useEffect, useState, useContext } from "react";
import { ShopContext } from "../../context/shop-context";
import { Product } from "./product";
import "./shop.css"

export const Shop = () => {
    const { cartItems, products, addToCart, removeFromCart, updateCartItemCount} = useContext(ShopContext);

    return <div className="shop">
        <div className="shopTitle">
            <h1>Mercado Moderno</h1>
        </div>
        <div className="products">
            {products.map((product) => <Product data={product} />)}
        </div>
    </div>
}