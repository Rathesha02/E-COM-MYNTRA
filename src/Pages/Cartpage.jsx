import React, { useEffect, useState } from "react";  
import axios from "axios";  
import "./Cartpage.css";  
import Navbar from "../Components/Navbar";  

const Cartpage = () => {
  const [cartItems, setCartItems] = useState([]);
  const userId = 1;

  useEffect(() => {
    const fetchCart = async () => {
      try {
        const res = await axios.get(`http://127.0.0.1:5000/api/cart/${userId}`);
        setCartItems(res.data);
      } catch (err) {
        console.error("❌ Fetch cart error:", err);
      }
    };
    fetchCart();
  }, []);

  const updateQuantity = async (product_id, newQty) => {
    if (newQty < 1) return;
    try {
      await axios.put("http://127.0.0.1:5000/api/cart", {
        user_id: userId,
        product_id,
        quantity: newQty,
      });
      setCartItems((prev) =>
        prev.map((item) =>
          item.product_id === product_id ? { ...item, quantity: newQty } : item
        )
      );
    } catch (err) {
      console.error("❌ Update quantity error:", err);
    }
  };
  
  const removeItem = async (product_id) => {
    try {
      await axios.delete("http://127.0.0.1:5000/api/cart", {
        data: { user_id: userId, product_id },
      });
      setCartItems((prev) => prev.filter((item) => item.product_id !== product_id));
    } catch (err) {
      console.error("❌ Remove item error:", err);
    }
  };
  
  return (
    <div>
     
      <div className="cart-container">
        <h2>🛒 Your Cart</h2>
        {cartItems.length === 0 ? (
          <p>No items in cart</p>
        ) : (
          cartItems.map((item) => (
            <div className="cart-item" key={item.product_id}>
              <img
                src={`http://127.0.0.1:5000/Static/Images/${item.product_image}`}
                alt={item.product_name}
                className="cart-image"
              />
              <div className="cart-details">
                <h3>{item.product_name}</h3>
                <p>
                  Price: ₹{item.product_price ? Number(item.product_price).toFixed(2) : "0.00"}
                </p>
                <p>Quantity: {item.quantity}</p>
                <div className="cart-actions">
                  <button onClick={() => updateQuantity(item.product_id, item.quantity + 1)}>➕</button>
                  <button onClick={() => updateQuantity(item.product_id, item.quantity - 1)}>➖</button>
                  <button className="remove-btn" onClick={() => removeItem(item.product_id)}>🗑 Remove</button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Cartpage;
