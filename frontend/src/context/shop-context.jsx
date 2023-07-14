import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

export const ShopContext = createContext(null)


export const ShopContextProvider = (props) => {
    const [cartItems, setCartItems] = useState({})
    const [products, setProducts] = useState([]);
    const [logged, setLogged] = useState(false);
    const [userId, setUserId] = useState(null);
    
    let cart = {};
    useEffect(() => {
        axios.get("http://127.0.0.1:8080/api/produtos/")
        .then((response) => {
            setProducts(response.data);

            response.data.map((item) => cart[item.id] = 0);

            if(logged) {
                axios.get(`http://127.0.0.1:8080/api/carrinhos/${userId}/produtos/`)
                .then((resp) => {
                    resp.data.map((item) => cart[item.produto] = item.quantidade)
                })
                .catch((erro) => console.log("erro ao tentar"))
            }
                
            setCartItems(cart);
        }).catch((error) => console.log(error));
    }, [logged]);
    
    const findProduct = (id) => {
        return products.find((p) => p.id === Number(id))
    }
    const addToCart = (itemId) => {
        cartItems[itemId] < findProduct(itemId)?.estoque ?
            setCartItems((prev) => {
                if(logged) {
                    axios.post(`http://localhost:8080/api/carrinhos/${userId}/produtos/add/`, {"produto_id": itemId, "quantidade": prev[itemId] + 1})
                    .catch((error) => console.log("Erro em addToCart."))
                }
                return ({ ...prev, [itemId]: prev[itemId] + 1})
            })

        : 
            alert(`Temos apenas ${cartItems[itemId]} unidades de ${findProduct(itemId)?.nome}!`);
    }
    const removeFromCart = (itemId) => {
        if(cartItems[itemId] > 0) {
            setCartItems((prev) => {
                if(logged) {
                    axios.post(`http://localhost:8080/api/carrinhos/${userId}/produtos/add/`, {"produto_id": itemId, "quantidade": prev[itemId] - 1})
                    .catch((error) => console.log("Erro em removeFromCart."))
                }
                return ({ ...prev, [itemId]: prev[itemId] - 1})
            })
        }
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
            
        setCartItems((prev) => {
            if(logged) {
                axios.post(`http://localhost:8080/api/carrinhos/${userId}/produtos/add/`, {"produto_id": itemId, "quantidade": amount})
                .catch((error) => console.log("Erro em removeFromCart."))
            }
            return ({ ...prev, [itemId]: amount})
        })
    };
    
    const checkout = async () => {
        if(logged) {
            axios.post(`http://127.0.0.1:8080/api/compras/${userId}/save`)
            .then((resp) => {
                products.map((p) => {
                    if(cartItems[p.id] > 0 && p.estoque - cartItems[p.id] >= 0) {
                        p.estoque -= cartItems[p.id];
                        p.vendas += cartItems[p.id];
                        setCartItems((prev) => ({...prev, [p.id]: 0}));
                    }
                    return p; 
                })
                setProducts(products);
                alert(`successful purchase, thanks for the preference!`)
            })
            .catch((erro) => console.log("Erro ao dar save"))
        } else {
            alert("Só é possível dar checkout logado");
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

    const contextValue = {cartItems, products, logged, setLogged, setUserId, addToCart, removeFromCart, checkout, updateCartItemCount, getTotalCartAmount}
    
    return <ShopContext.Provider value={contextValue}>
        {props.children}
    </ShopContext.Provider>
}