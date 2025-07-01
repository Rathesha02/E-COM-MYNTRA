import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Orders.css";

const Orders = () => {
  const [orders, setOrders] = useState([]);
  const userId = 1; // 🔁 Replace with dynamic login session user

  const fetchOrders = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/api/orders", {
        params: { user_id: userId },
        withCredentials: true,
      });
      setOrders(res.data);
    } catch (error) {
      console.error("❌ Failed to fetch orders", error);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  return (
    <div className="orders-wrapper">
      <h2>🛒 My Orders ({orders.length} items)</h2>

      {orders.map((order) => (
        <div className="order-card" key={order.order_id}>
          <div className="order-left">
            <img
              src={`http://127.0.0.1:5000/Static/Images/${order.product_image}`}
              alt={order.product_name}
              className="order-img"
            />
          </div>

          <div className="order-center">
            <h3>{order.product_name}</h3>
            <p>Order ID: #{order.order_id}</p>
            <p>Status: <strong>{order.status}</strong></p>
            <p>Quantity: {order.quantity}</p>
            <p>Delivery Address: {order.delivery_address}</p>
            <p>Payment Method: {order.payment}</p>
            <p>Ordered On: {new Date(order.created_at).toLocaleString()}</p>
          </div>

          <div className="order-right">
            <span className="price-label">Total Price</span>
            <h3>₹ {order.total_price}</h3>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Orders;
