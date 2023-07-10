import { React, useContext } from "react";
import { ShopContext } from "../../context/shop-context";
import { Product } from "./product";
import "./shop.css"

export const Shop = () => {
    const { products } = useContext(ShopContext);

    return <div className="shop">
        <div className="shopTitle">
            <h1>Mercado Moderno</h1>
        </div>
        <div className="products">
            {products.map((prod) => prod.estoque > 0 && <Product data={prod} />)}
        </div>
    </div>
}