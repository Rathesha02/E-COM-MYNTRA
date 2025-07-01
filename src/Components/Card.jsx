import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./Card.css";

function Card() {
  const [products, setProducts] = useState([]);
  const navigate = useNavigate();
  const userId = 1; // 🔁 Replace with dynamic user ID later

  // ✅ Fetch products from Flask backend
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:5000/api/products");
        console.log("🚀 Products:", res.data);

        if (Array.isArray(res.data)) {
          setProducts(res.data);
        } else {
          console.warn("Unexpected response:", res.data);
          setProducts([]);
        }
      } catch (error) {
        console.error("❌ Error fetching products:", error);
        setProducts([]);
      }
    };

    fetchProducts();
  }, []);

  // ✅ Add to cart handler
  const handleAddToCart = async (product) => {
    const cartData = {
      user_id: userId,
      product_id: product.productid,
      product_name: product.name,
      product_image: product.image,
      product_price: product.price,
      stock: product.stock,
      quantity: 1,
    };

    try {
      const res = await axios.post("http://127.0.0.1:5000/api/cart", cartData);
      console.log("✅ Cart response:", res.data);
      alert("✅ Product added to cart!");
    } catch (error) {
      console.error("❌ Error adding to cart:", error);
      alert("❌ Failed to add to cart.");
    }
  };

  // ✅ Buy Now / Place Order handler
  const handleBuyNow = async (product) => {
    try {
      const orderData = {
        user_id: userId,
        product_id: product.productid,
        product_name: product.name,
        product_price: product.price,
        product_image: product.image,
        quantity: 1,
        total_price: product.price * 1,
        delivery_address: "123, Main Road, Chennai", // 🔁 make dynamic later
        payment: "COD",
        status: "pending",
      };

      const res = await axios.post("http://127.0.0.1:5000/api/orders", orderData, {
        withCredentials: true,
      });

      console.log("✅ Order Placed:", res.data);
      alert("✅ Order placed successfully!");
    } catch (error) {
      console.error("❌ Failed to place order:", error);
      alert("❌ Failed to place order. Check console for error.");
    }
  };

  return (
    <div className="card-container">
      {products.length === 0 ? (
        <p>No products available</p>
      ) : (
        products.map((product) => (
          <div className="card" key={product.productid}>
            <img
              src={
                product.image
                  ? `http://127.0.0.1:5000/Static/Images/${product.image}`
                  : "https://via.placeholder.com/200x200?text=No+Image"
              }
              alt={product.name || "Product"}
            />
            <div className="card-content">
              <h2>{product.name}</h2>
              <p className="price">Rs. {product.price}</p>
              <p className="stock">
                <strong>In stock:</strong> {product.stock}
              </p>
              <p className="description">{product.description}</p>
              <div className="button-group">
                <button onClick={() => handleAddToCart(product)}>Add to Cart</button>
                <button className="buy-now" onClick={() => handleBuyNow(product)}>
                  Buy Now
                </button>
              </div>
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default Card;
