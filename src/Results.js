import React from 'react';

function ResultsPage({ results }) {
  return (
    <div className="results-page">
      <h1>Search Results</h1>
      <ul>
        {results.map((result, index) => (
          <li key={index}>{result}</li>
        ))}
      </ul>
    </div>
  );
}

export default ResultsPage;
