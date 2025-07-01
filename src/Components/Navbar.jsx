import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Navbar.css';
import { Button } from 'bootstrap/dist/js/bootstrap.bundle.min';

function Navbar() {
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate();

  const handleSearch = (e) => {
    if (e.key === 'Enter' && searchTerm.trim() !== '') {
      navigate(`/search/${searchTerm}`);
    }
  };

  return (
    <nav className="navbar">
      {/* Left: Home, Cart, Orders, Admin, Profile */}
      <div className="navbar-left">
        <img src="M5.jpeg.png" alt="Logo" className="logo" />
        <ul className="nav-links">
          <li><Link to="/">🏠HOME</Link></li>
          <li><Link to="/cart">🛒Cart</Link></li>
          <li><Link to="/orders">📦Orders</Link></li>
         

          <li><Link to="/login">🧑‍💻Admin</Link></li>
          <li><Link to="/User">🔐UserLogin</Link></li>
        </ul>
      </div>

      {/* Right: Search Bar */}
      <div className="navbar-right">
        <div className="search-box">
          <span className="search-icon">🔍</span>
          <input
            type="text"
            placeholder="Search for products, brands and more"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyDown={handleSearch}
          />
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
