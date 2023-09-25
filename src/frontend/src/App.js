import React, { useEffect, useState } from 'react'; 

import logo from './logo.svg';
import './App.css';

function App() {
  const [loading, setLoading] = useState(true);
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch(
      'http://localhost:8000/api/main/'
    ).then(res => {
      const data = res.data;
      setLoading(false);
      setSuccess(true);
      return data.json();
    })
    .catch(err => {
      setLoading(false);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {!loading && success && (
          <>
            <img src={logo} className="App-logo" alt="logo" />
            <p>
              Edit <code>src/App.js</code> and save to reload.
            </p>
            <a
              className="App-link"
              href="https://reactjs.org"
              target="_blank"
              rel="noopener noreferrer"
            >
              Learn React
            </a>
          </>
        )}
      </header>
    </div>
  );
}

export default App;
