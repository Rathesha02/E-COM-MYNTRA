import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';


const SearchPage = () => {
  const { keyword } = useParams();
  const [results, setResults] = useState([]);

  useEffect(() => {
    const fetchSearchResults = async () => {
      const res = await axios.get(`http://localhost:5000/products`);
      const filtered = res.data.filter((item) =>
        item.name.toLowerCase().includes(keyword.toLowerCase())
      );
      setResults(filtered);
    };
    fetchSearchResults();
  }, [keyword]);

  return (
    <div className="search-results">
      <h2>Results for: "{keyword}"</h2>
      <div className="card-container">
        {results.length > 0 ? (
          results.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))
        ) : (
          <p>No products found.</p>
        )}
      </div>
    </div>
  );
};

export default SearchPage;
