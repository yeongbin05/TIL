import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './App.jsx';
import AlgorithmList from './pages/algorithm/AlgorithmList.jsx';
import AlgorithmDetail from './pages/algorithm/AlgorithmDetail.jsx';
import CsList from './pages/cs/CsList.jsx';
import CsDetail from './pages/cs/CsDetail.jsx';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <Router>
    <Routes>
      <Route path="/*" element={<App />} />
      <Route path="/algorithm" element={<AlgorithmList />} />
      <Route path="/algorithm/:id" element={<AlgorithmDetail />} />
      <Route path="/cs/" element={<CsList />} />
      <Route path="/cs/:id" element={<CsDetail />} />
    </Routes>
  </Router>
);
