// pages/algorithm/AlgorithmList.jsx
import React, { useEffect, useState } from 'react';
import './AlgorithmList.css';
import AlgorithmCard from '../../components/Algorithm/AlgorithmCard';
import Header from '../../components/Header/Header';
import { useNavigate } from 'react-router-dom';

function AlgorithmList() {
  const [algorithms, setAlgorithms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedTag, setSelectedTag] = useState('전체');
  const navigate = useNavigate();

  useEffect(() => {
    const path = process.env.PUBLIC_URL + '/data/algorithm/index.json';

    fetch(path)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return res.json();
      })
      .then((data) => setAlgorithms(data))
      .catch((err) => console.error('❌ fetch 실패:', err))
      .finally(() => setLoading(false));
  }, []);

  const handleCardClick = (id) => {
    navigate(`/algorithm/${id}`);
  };

  const allTags = ['전체', ...new Set(algorithms.flatMap((algo) => algo.tags))];

  const filteredAlgorithms =
    selectedTag === '전체'
      ? algorithms
      : algorithms.filter((algo) => algo.tags.includes(selectedTag));

  return (
    <div className="algorithm-list-wrapper">
      <Header />
      <main className="algorithm-main">
        <div className="tag-sidebar">
          <h3 className="tag-sidebar-title">📌 태그 필터</h3>
          {allTags.map((tag) => (
            <button
              key={tag}
              className={`tag-button ${selectedTag === tag ? 'active' : ''}`}
              onClick={() => setSelectedTag(tag)}
            >
              {tag}
            </button>
          ))}
        </div>

        <div className="algorithm-content">
          <h2 className="algorithm-list-title">📘 알고리즘 문제 목록</h2>
          {loading ? (
            <p style={{ color: 'white', padding: '1rem' }}>불러오는 중...</p>
          ) : (
            <div className="algorithm-list">
              {filteredAlgorithms.map((item) => (
                <div
                  key={item.id}
                  onClick={() => handleCardClick(item.id)}
                  style={{ cursor: 'pointer' }}
                  role="button"
                  tabIndex={0}
                  onKeyDown={(e) =>
                    e.key === 'Enter' && handleCardClick(item.id)
                  }
                >
                  <AlgorithmCard data={item} />
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default AlgorithmList;
