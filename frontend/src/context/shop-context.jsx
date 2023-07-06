import React, { createContext, useState, useEffect } from "react";
import { PRODUCTS } from "../products";
import axios from "axios";

export const ShopContext = createContext(null)


export const ShopContextProvider = (props) => {
    // {id: number of items of allItems[id]}
    const [cartItems, setCartItems] = useState({})
    const [products, setProducts] = useState([]);
    
    let cart = {};
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/produtos/").then((response) => {
                setProducts(response.data);
                response.data.map((item) => cart[item.id] = 0);
                setCartItems(cart);
        });
    }, []);

    const addToCart = (itemId) => {
        setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId] + 1}))
    }
    const removeFromCart = (itemId) => {
        setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId] - 1}))
    }

    const updateCartItemCount = (newAmount, itemId) => {
        setCartItems((prev) => ({ ...prev, [itemId]: newAmount}))
    };

    const getTotalCartAmount = () => {
        let totalAmount = 0;

        for(const item in cartItems) {
            if (cartItems[item] > 0) {
                let itemInfo = products.find((product) => product.id === Number(item));
                totalAmount += cartItems[item] * itemInfo?.preco;
            }
        }

        return totalAmount;
    }

    const contextValue = {cartItems, products, addToCart, removeFromCart, updateCartItemCount, getTotalCartAmount}
    
    return <ShopContext.Provider value={contextValue}>
        {props.children}
    </ShopContext.Provider>
}