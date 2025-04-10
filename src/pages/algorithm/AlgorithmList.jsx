// pages/algorithm/AlgorithmList.jsx
import React, { useEffect, useState } from 'react';
import './AlgorithmList.css';
import AlgorithmCard from '../../components/Algorithm/AlgorithmCard';
import Header from '../../components/Header/Header';
import { useNavigate } from 'react-router-dom';

function AlgorithmList() {
  const [algorithms, setAlgorithms] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const path = process.env.PUBLIC_URL + '/data/algorithm/index.json';

    fetch(path)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setAlgorithms(data);
      })
      .catch((err) => console.error('❌ fetch 실패:', err))
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const handleCardClick = (id) => {
    navigate(`/algorithm/${id}`);
  };

  return (
    <div className="algorithm-list-wrapper">
      <Header />
      <h2 className="algorithm-list-title">📘 알고리즘 문제 목록</h2>

      {loading ? (
        <p style={{ color: 'white', padding: '1rem' }}>불러오는 중...</p>
      ) : (
        <div className="algorithm-list">
          {algorithms.map((item) => (
            <div
              key={item.id}
              onClick={() => handleCardClick(item.id)}
              style={{ cursor: 'pointer' }}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === 'Enter' && handleCardClick(item.id)}
            >
              <AlgorithmCard data={item} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default AlgorithmList;
