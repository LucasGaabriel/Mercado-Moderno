import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

export const ShopContext = createContext(null)


export const ShopContextProvider = (props) => {
    // {id: number of items of allItems[id]}
    const [cartItems, setCartItems] = useState({})
    const [products, setProducts] = useState([]);
    const [updated, setUpdated] = useState(false);
    
    let cart = {};
    useEffect(() => {
        axios.get("http://127.0.0.1:8080/api/produtos/").then((response) => {
                setProducts(response.data);
                response.data.map((item) => cart[item.id] = 0);
                setCartItems(cart);
        });
    }, []);
    //
    const findProduct = (id) => {
        return products.find((p) => p.id === Number(id))
    }
    const addToCart = (itemId) => {
        cartItems[itemId] < findProduct(itemId)?.estoque ?
            setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId] + 1}))
        : 
            alert(`Temos apenas ${cartItems[itemId]} unidades de ${findProduct(itemId)?.nome}!`);
    }
    const removeFromCart = (itemId) => {
        cartItems[itemId] > 0 &&
            setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId] - 1}))
        cartItems[itemId] === 1 &&
            alert(`${findProduct(itemId)?.nome} removido(a) do carrinho`);
    }

    const updateCartItemCount = (newAmount, itemId) => {
        let amount = Number(newAmount);
        let estoque = findProduct(itemId)?.estoque;

        if (amount > estoque)
            amount = estoque;
        else if(amount < 0)
            amount = 0;
            
        setCartItems((prev) => ({ ...prev, [itemId]: amount}))
    };
    
    const checkout = async () => {
        try { 
            products.map((p) => {
                if(cartItems[p.id] > 0) {
                    axios.patch(`http://127.0.0.1:8080/api/produtos/${p.id}/`, { 
                        estoque: p.estoque - cartItems[p.id],
                        vendas: p.vendas + cartItems[p.id]
                    });
                    p.estoque -= cartItems[p.id];
                    p.vendas += cartItems[p.id];
                    setCartItems((prev) => ({...prev, [p.id]: 0}));
                }  
            })
            
            setProducts(products);
        } catch (error) {
            console.error(error);
        }
    }

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

    const contextValue = {cartItems, products, addToCart, removeFromCart, checkout, updateCartItemCount, getTotalCartAmount}
    
    return <ShopContext.Provider value={contextValue}>
        {props.children}
    </ShopContext.Provider>
}