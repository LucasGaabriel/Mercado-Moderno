import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Navbar } from "./components/navbar"
import { Shop } from "./pages/shop/shop"
import { Cart } from "./pages/cart/cart"
import { Login } from "./pages/login/Login"
import { Register } from "./pages/register/Register"
import { ShopContextProvider } from './context/shop-context';

function App() {
  return (
    <div className="App">
      {/* Provide the shop context to the components */}
      <ShopContextProvider>
        {/* Set up the router */}
        <Router>
          {/* Render the navbar */}
          <Navbar />
          {/* Define the routes*/}
          <Routes>
            {/* Render the Shop component in path "/" */}
            <Route path="/" element={<Shop />} />
            {/* Render the Cart component in path "/cart" */}
            <Route path="/cart" element={<Cart />}  /> 
            {/* Render the Login component in path "/login" */}
            <Route path="/login" element={<Login />}  /> 
            {/* Render the Register component in path "/register" */}
            <Route path="/register" element={<Register />}  /> 
          </Routes>
        </Router>
      </ShopContextProvider>
    </div>
  );
}

export default App;
