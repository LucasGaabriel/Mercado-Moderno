import axios from "axios";
import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import { PRODUCTS } from "../../products";
import { Product } from "./product";
import "./shop.css"

export const Shop = () => {
    const [products, setProducts] = useState([]);
    
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/produtos/").then((response) => {
                setProducts(response.data);
        });
    }, []);
    //console.log(products);

    return <div className="shop">
        <div className="shopTitle">
            <h1>Mercado Moderno</h1>
        </div>
        <div className="products">
            {products.map((product) => <Product data={product} />)}
        </div>
    </div>
}