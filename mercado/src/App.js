import './App.css';
import { Form } from './Form'
import { useState } from "react"
import { useForm } from "react-hook-form"

function App() {
  const [allProducts, setAllProducts] = useState([]);
  const [showForm, setShowForm] = useState(0);    // Fazer showForm guardar o ID
  const [editingProductId, setEditingProductId] = useState(null); // Track the ID of the product being edited
  const { register, handleSubmit } = useForm()

  const onSubmit = (data) => {
    if (editingProductId !== null) {
      // Editing an existing product
      const updatedProducts = allProducts.map((product) => {
        if (product.id === editingProductId) {
          console.log(data)
          return { ...product, ...data };
        }
        return product;
      });
      setAllProducts(updatedProducts);
      setEditingProductId(null);
    } else if(showForm === 1) {
      let product = {
        id: allProducts.length,
        description: data.description,
        price: data.price,
        discount: data.discount,
        sales_counter: 0,
        qtt_stock: data.qtt_stock,
        IsAvailable: true
      }
      
      setAllProducts([...allProducts, product])
      setShowForm(0)
    }
  }

  const editProduct = (id) => {
    const product = allProducts.find((p) => p.id === id);
    if (product) {
      setEditingProductId(id);
      setShowForm(2);
    }
  };

  return (
    <div className="App"> 
      <div className="Register_Product">
        <button onClick={() => setShowForm(1)}>Add Product</button>
        {showForm===1 && <Form register={register} handleSubmit={handleSubmit} onSubmit={onSubmit}/> }
      </div>
      <div className="Show_Products">
        {allProducts.map((product) => {
          return <div key={product.id}>
            <h1>{`${product.description} (${product.qtt_stock})`}</h1>
            <button onClick={() => editProduct(product.id)}>Edit</button>
            <button>Add Cart</button>
            {showForm===2 && <Form register={register} handleSubmit={handleSubmit} onSubmit={onSubmit}/> }
          </div>
        })}
      </div>
    </div>
  );
}

export default App;
