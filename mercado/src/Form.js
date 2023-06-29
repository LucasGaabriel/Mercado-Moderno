export const Form = (props) => {

    return <form onSubmit={props.handleSubmit(props.onSubmit)}>
        <input type="text" placeholder="Description..." {...props.register("description")}/>
        <input type="number" placeholder="price..." {...props.register("price")}/>
        <input type="number" placeholder="Discount..." {...props.register("discount")}/>
        <input type="number" placeholder="Quantity in Stock..." {...props.register("qtt_stock")}/>
        <input type="submit" />
    </form>
}
