import React, { useEffect, useState } from 'react';
import CsCard from '../../components/CS/CsCard';
import Header from '../../components/Header/Header';
import './CsList.css';

function CsList() {
  const [csData, setCsData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const path = process.env.PUBLIC_URL + '/data/cs/cs.json';

    fetch(path)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setCsData(data);
      })
      .catch((err) => console.error('❌ fetch 실패:', err))
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="cs-list-wrapper">
      <Header />
      <h2 className="cs-list-title">📘 CS 자료 목록</h2>

      {loading ? (
        <p style={{ color: 'white', padding: '1rem' }}>불러오는 중...</p>
      ) : (
        <div className="cs-list">
          {csData.map((item) => (
            <CsCard key={item.id} data={item} />
          ))}
        </div>
      )}
    </div>
  );
}

export default CsList;
