import React from "react";
import { Routes, Route } from "react-router-dom";

// Components
import Navbar from "./Components/Navbar";
import Footer from "./Components/Footer";

// Pages
import Home from "./Pages/Home";
import Orders from "./Pages/Orders";
import Cartpage from "./Pages/Cartpage";
import Admin from "./Pages/Admin";
import Login from './Pages/Login';
import User from './Pages/User'; 

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/cart" element={<Cartpage />} />
         <Route path="/login" element={<Login />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/orders" element={<Orders />} />
        <Route path="/User" element={<User />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
