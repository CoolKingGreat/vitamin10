import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [quote, setQuote] = useState('');

  const fetchQuote = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/quote');
      const data = await response.json();
      setQuote(data.quote);
    } catch (error) {
      console.error("Error fetching quote:", error);
    }
  };

  useEffect(() => {
    fetchQuote();
  }, []);

  return (
    <div className="App">
      <div className="quote-box">
        <h1>Quote of the Day</h1>
        <button onClick={fetchQuote}>Get Quote</button>
        <p className="quote-text">{quote}</p>
      </div>
    </div>
  );
}

export default App;