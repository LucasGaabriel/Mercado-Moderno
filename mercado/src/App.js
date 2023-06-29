import './App.css';
import { Form } from './Form'
import { useState } from "react"
import { useForm } from "react-hook-form"

function App() {
  const [allProducts, setAllProducts] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const { register, handleSubmit } = useForm()

  const onSubmit = (data) => {
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
    setShowForm(false)
  }

  return (
    <div className="App"> 
      <div className="Register_Product">
        <button onClick={() => setShowForm(true)}>Add Product</button>
        {showForm && <Form register={register} handleSubmit={handleSubmit} onSubmit={onSubmit}/> }
      </div>
      <div className="Show_Products">
        {allProducts.map((product) => {
          return <div>
            <h1>{`${product.description} (${product.qtt_stock})`}</h1>
            <button>Edit</button>
            <button>Add Cart</button>
          </div>
        })}
      </div>
    </div>
  );
}

export default App;
