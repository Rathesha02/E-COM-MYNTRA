// src/Pages/Admin.jsx

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Navbar from '../Components/Navbar';
import './Admin.css';

const API_BASE = 'http://127.0.0.1:5000/api/products';

const Admin = () => {
  const navigate = useNavigate();

  const [products, setProducts] = useState([]);
  const [form, setForm] = useState({
    name: '', price: '', stock: '', image: null, description: '', category: ''
  });
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(true);

  // ✅ Redirect to login if not logged in
  useEffect(() => {
    const isAdmin = localStorage.getItem('adminLoggedIn');
    if (!isAdmin) {
      navigate('/login');
    }
  }, [navigate]);

  const fetchProducts = async () => {
    try {
      const res = await axios.get(API_BASE);
      setProducts(res.data);
    } catch (error) {
      console.error('Error fetching products', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (name === 'image') {
      setForm({ ...form, image: files[0] });
    } else {
      setForm({ ...form, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', form.name);
    formData.append('price', form.price);
    formData.append('stock', form.stock);
    formData.append('description', form.description);
    formData.append('category', form.category);
    if (form.image) {
      formData.append('image', form.image);
    }

    const config = { headers: { 'Content-Type': 'multipart/form-data' } };
    try {
      if (editingId) {
        await axios.put(`${API_BASE}/${editingId}`, formData, config);
      } else {
        await axios.post(API_BASE, formData, config);
      }
      setForm({ name: '', price: '', stock: '', image: null, description: '', category: '' });
      setEditingId(null);
      fetchProducts();
    } catch (error) {
      console.error(error);
    }
  };

  const handleEdit = (product) => {
    setForm({ ...product, image: null });
    setEditingId(product.productid);
  };

  const handleDelete = async (productId) => {
    if (window.confirm('Are you sure you want to delete this product?')) {
      await axios.delete(`${API_BASE}/${productId}`);
      fetchProducts();
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('adminLoggedIn');
    navigate('/login');
  };

  return (
    <div className="admin-container">
      

      <div className="admin-header">
        <h2>🧑‍💻 Admin Product Manager</h2>
        <button onClick={handleLogout} className="logout-button">Logout</button>
      </div>

      <form className="product-form" onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" value={form.name} onChange={handleChange} required />
        <input name="price" placeholder="Price" value={form.price} onChange={handleChange} required />
        <input name="stock" placeholder="Stock" value={form.stock} onChange={handleChange} required />
        <input type="file" name="image" accept="image/*" onChange={handleChange} required={!editingId} />
        <input name="description" placeholder="Description" value={form.description} onChange={handleChange} required />
        <input name="category" placeholder="Category" value={form.category} onChange={handleChange} required />
        <button type="submit">{editingId ? 'Update' : 'Add'} Product</button>
      </form>

      <h3>📦 All Products</h3>
      {loading && <p>Loading products…</p>}

      <div className="table-wrapper">
        <table className="products-table">
          <thead>
            <tr>
              <th>ID</th><th>Name</th><th>Price</th><th>Stock</th><th>Image</th><th>Description</th><th>Category</th><th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {products.map(prod => (
              <tr key={prod.productid}>
                <td>{prod.productid}</td>
                <td>{prod.name}</td>
                <td>₹{prod.price}</td>
                <td>{prod.stock}</td>
                <td>
                  <img
                    src={`http://127.0.0.1:5000/static/uploads/${prod.image}`}
                    alt={prod.name}
                    onError={(e) => { e.target.onerror = null; e.target.src = 'https://via.placeholder.com/50'; }}
                    width="50"
                  />
                </td>
                <td>{prod.description}</td>
                <td>{prod.category}</td>
                <td>
                  <div className="actions">
                    <button className="edit-button" onClick={() => handleEdit(prod)}>Edit</button>
                    <button className="delete-button" onClick={() => handleDelete(prod.productid)}>Delete</button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Admin;
