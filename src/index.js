import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './App';
import AlgorithmList from './components/Algorithm/AlgorithmList';
import AlgorithmDetail from './components/Algorithm/AlgorithmDetail';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <Router>
    <Routes>
      <Route path="/*" element={<App />} />
      <Route path="/algorithm" element={<AlgorithmList />} />
      <Route path="/algorithm/:id" element={<AlgorithmDetail />} />
    </Routes>
  </Router>
);
