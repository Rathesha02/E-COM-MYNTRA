import React from 'react';
import Navbar from '../Components/Navbar';
import Carousel from '../Components/Carousel';
import Card from '../Components/Card';
import Footer from '../Components/Footer';

const Home = () => {
  return (
    <div>
      
      <h2 style={{ textAlign: 'center', marginTop: '20px' }}>
                Welcome to Myntra 💗 – Your Fashion Destination!!!
              </h2>
              <Carousel />
              <Card />
              
    </div>
  );
};

export default Home;
