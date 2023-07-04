import React, { createContext, useState } from "react";
import { PRODUCTS } from "../products";

export const ShopContext = createContext(null)

// Usar o ID do Product -------------------------------
const getDefaultCart = () => {
    let cart = {}
    for (let i=0; i< PRODUCTS.length; i++) {
        cart[PRODUCTS[i].id] = {...PRODUCTS[i], qtt_cart: 0 };
        console.log(cart[PRODUCTS[i].id].productName)
    }
    return cart;
}

export const ShopContextProvider = (props) => {
    const [cartItems, setCartItems] = useState(getDefaultCart())

    const addToCart = (itemId) => {
        setCartItems((prev) => ({ ...prev, [itemId]: {...prev[itemId], qtt_cart: qtt_cart + 1}}));
    }
    const removeFromCart = (itemId) => {
        setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId].qtt_cart - 1}));
    }

    const updateCartItemCount = (newAmount, itemId) => {
        setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId].qtt_cartnewAmount }));
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

    const contextValue = {cartItems, addToCart, removeFromCart, updateCartItemCount, getTotalCartAmount}

    return <ShopContext.Provider value={contextValue}>
        {props.children}
    </ShopContext.Provider>
}