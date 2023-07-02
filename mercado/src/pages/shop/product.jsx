import React from "react";

export const Product = (props) => {
    const {id, productName, price, qtt_stock, qtt_sells, productImage} = props.data;

    return <div className="product">
        <img src={productImage}/>
        <div className="description">
            <p>
                <b>{productName}</b>
            </p>
            <p>{price}</p>
        </div>
        <button className="addToCarbtn">Add To Cart</button>
    </div>
}