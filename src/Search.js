import React, { useState } from 'react';

export default function HomePage() {
  const [searchTerm, setSearchTerm] = useState('');

  const handleInputChange = (e) => {
    setSearchTerm(e.target.value);
  }

  const handleSearch = () => {
    // Add your search functionality here
    console.log('Searching for:', searchTerm);
    // You can perform any search actions with `searchTerm` here
  }

  return (
    <div className="homepage">
      <h1>Welcome to the Search Page</h1>
      <div className="search-container">
        <input 
          type="text" 
          placeholder="Search..." 
          value={searchTerm} 
          onChange={handleInputChange} 
        />
        <button onClick={handleSearch}>Search</button>
      </div>
    </div>
  );
}

HomePage;
