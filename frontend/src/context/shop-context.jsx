import React, { createContext, useState, useEffect } from "react";
import { PRODUCTS } from "../products";
import axios from "axios";

export const ShopContext = createContext(null)


export const ShopContextProvider = (props) => {
    // {id: number of items of allItems[id]}
    const [cartNumberItems, setCartNumberItems] = useState({})
    
    let cart = {};
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/produtos/").then((response) => {
            response.data.map((item) => cart[item.id] = item);
            console.log(cart);
        });

    }, []);
    //console.log(products);

    /*const addToCart = (itemId) => {
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
                let itemInfo = PRODUCTS.find((product) => product.id === Number(item));
                totalAmount += cartItems[item] * itemInfo?.price;
            }
        }

        return totalAmount;
    }
    */
    const contextValue = {cartNumberItems, /*addToCart, removeFromCart, updateCartItemCount, getTotalCartAmount*/}
    
    return <ShopContext.Provider value={contextValue}>
        {props.children}
    </ShopContext.Provider>
}