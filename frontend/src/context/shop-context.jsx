import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

// Create a context for the shop state
export const ShopContext = createContext(null)


export const ShopContextProvider = (props) => {
    // State variables for store values from server
    const [cartItems, setCartItems] = useState({})
    const [products, setProducts] = useState([]);
    const [logged, setLogged] = useState(false);
    const [userId, setUserId] = useState(null);
    
    let cart = {};
    
    // Fetch products and cart items when the 'logged' 
    // and fill cartItems and products with current values.
    useEffect(() => {
        axios.get("http://127.0.0.1:8080/api/produtos/")
        .then((response) => {
            // Set the products with the fetched data
            setProducts(response.data);

            if(logged) {
                // Fill the user cart with the user guest cart
                for(const idItem in cartItems) {
                    if (cartItems[idItem] > 0) {
                        axios.post(`http://localhost:8080/api/carrinhos/${userId}/produtos/add/`, {"produto_id": idItem, "quantidade": cartItems[idItem]})
                        .catch((error) => console.log("Erro em fillUserCart"))
                    }
                }

                // Fill cartItems with the user cart
                axios.get(`http://127.0.0.1:8080/api/carrinhos/${userId}/produtos/`)
                .then((resp) => {
                    // User cart
                    resp.data.map((item) => cart[item.produto] = item.quantidade)

                    // Others fill with 0
                    response.data.map((item) => typeof cart[item.id] === 'undefined' ? cart[item.id] = 0 : cart[item.id]);

                    // Set the cartItems with the cart object
                    setCartItems(cart);
                })
                .catch((erro) => console.log("erro ao tentar"))
            } else {
                // Fill the guest cart with 0
                response.data.map((item) => cart[item.id] = 0 );

                // Set the cartItems with the cart object
                setCartItems(cart);
            }
        }).catch((error) => console.log(error));
    }, [logged]);

  
    // Find a product from products by id
    const findProduct = (id) => {
        return products.find((p) => p.id === Number(id))
    }

    // Add an unit of product from the cart and
    // from the produtos in api
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
    
    // remove an unit of product from the cart and
    // from the produtos in api
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
        // Send a alert to the user when they remove a item
        cartItems[itemId] === 1 &&
            alert(`${findProduct(itemId)?.nome} removido(a) do carrinho`);
    }

    // Update the quantity of an item in
    // the cart and in the products api
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
    
    // Updates the values of 'estoque' and 'vendas' in products,
    // set the cartItems to empty and do all the
    // changes in the api that 'save' post operation does
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

    // Calculate the total amount of the cart
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

    // Selects the values ​​that will be shared using context
    const contextValue = {cartItems, products, logged, setLogged, setUserId, addToCart, removeFromCart, checkout, updateCartItemCount, getTotalCartAmount}
    
    
    return (
        // Provide the context value to the children components
        <ShopContext.Provider value={contextValue}>
            {props.children}
        </ShopContext.Provider>
    )
}