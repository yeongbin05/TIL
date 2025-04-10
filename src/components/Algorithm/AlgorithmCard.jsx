// components/Algorithm/AlgorithmCard.jsx
import React from 'react';
import './AlgorithmCard.css';

function AlgorithmCard({ data }) {
  const { id, title, description, tags, thumbnail } = data;

  const truncate = (text, maxLength) => {
    if (!text) return '';
    return text.length > maxLength ? text.slice(0, maxLength) + '...' : text;
  };

  const platform = id.split('/')[0];

  const defaultThumbnails = {
    boj: '/baekjoon-default.png',
    leetcode: '/leetcode-default.png',
  };

  const handleImageError = (e) => {
    const fallback = defaultThumbnails[platform] || '/default-thumbnail.png';
    e.target.src = process.env.PUBLIC_URL + fallback;
  };

  return (
    <div className="algorithm-card">
      <img
        src={`${process.env.PUBLIC_URL}${thumbnail}`}
        alt={title}
        className="algorithm-thumbnail"
        onError={handleImageError}
      />
      <h3 className="algorithm-title">{title}</h3>
      <p className="algorithm-description">{truncate(description, 100)}</p>
      <div className="algorithm-tags">
        {tags?.map((tag, index) => (
          <span key={index} className="algorithm-tag">{tag}</span>
        ))}
      </div>
    </div>
  );
}

export default AlgorithmCard;
