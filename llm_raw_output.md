# LLM Output

=== FILE: src/App.jsx ===
import React, { useState } from 'react';
import { HashRouter, Routes, Route, Link } from 'react-router-dom';
import axios from '../api';
import './index.css';

function Calculator() {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [operator, setOperator] = useState('+');
  const [result, setResult] = useState(0);

  const calculate = async () => {
    try {
      const response = await axios.post('/calculate', { num1, num2, operator });
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="container mx-auto p-4 pt-6 md:p-6 lg:p-12 xl:p-24">
      <h1 className="text-3xl font-bold mb-4">Mathematics Calculator</h1>
      <form>
        <div className="flex flex-wrap -mx-3 mb-2">
          <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              Number 1
            </label>
            <input
              className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              type="number"
              value={num1}
              onChange={(e) => setNum1(Number(e.target.value))}
            />
          </div>
          <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              Operator
            </label>
            <select
              className="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              value={operator}
              onChange={(e) => setOperator(e.target.value)}
            >
              <option value="+">+</option>
              <option value="-">-</option>
              <option value="*">*</option>
              <option value="/">/</option>
            </select>
          </div>
          <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
            <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
              Number 2
            </label>
            <input
              className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              type="number"
              value={num2}
              onChange={(e) => setNum2(Number(e.target.value))}
            />
          </div>
        </div>
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="button"
          onClick={calculate}
        >
          Calculate
        </button>
      </form>
      <p className="text-lg font-bold mt-4">Result: {result}</p>
    </div>
  );
}

function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Calculator />} />
      </Routes>
    </HashRouter>
  );
}

export default App;
=== END ===

=== FILE: src/main.jsx ===
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
=== END ===

=== FILE: src/index.css ===
@tailwind base;
@tailwind components;
@tailwind utilities;
=== END ===

=== FILE: src/api.js ===
import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: BASE_URL,
});

export default api;
=== END ===