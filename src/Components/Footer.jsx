import React from 'react';


const Footer = () => {
  return (
    <footer className="footer-full text-center py-4">
      <div className="container text-white">
        <h4 className="mb-2">🛒 Myntra Online Shopping</h4>
        <h5 className="mb-1">🔥 50% Ethnic Offers</h5>
        <p className="footer-text">
          Discover stylish fashion and affordable electronics.<br />
          Trusted by thousands of happy customers!
        </p>
        <a href="/offers" className="btn btn-warning text-dark my-3 px-4 fw-bold">
          Explore Offers⚡
        </a>
        <h3 className="mt-4 mb-0 small">✨ Thank you for visiting. Come again! ✨</h3>
      </div>
    </footer>
  );
};

export default Footer;
