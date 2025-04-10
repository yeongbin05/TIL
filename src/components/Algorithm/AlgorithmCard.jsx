import React from 'react';
import { Link } from 'react-router-dom';
import './AlgorithmCard.css';

function AlgorithmCard({ data }) {
  const { id, title, description, tags, thumbnail } = data;

  const truncate = (text, maxLength) => {
    if (!text) return '';
    return text.length > maxLength ? text.slice(0, maxLength) + '...' : text;
  };

  return (
    <Link to={`/algorithm/${id}`} className="algorithm-card-link">
      <div className="algorithm-card">
        {thumbnail && (
          <img
            src={`${process.env.PUBLIC_URL}${thumbnail}`}
            alt={title}
            className="algorithm-thumbnail"
          />
        )}
        <h3 className="algorithm-title">{title}</h3>
        <p className="algorithm-description">{truncate(description, 100)}</p>
        <div className="algorithm-tags">
          {tags && tags.map((tag, index) => (
            <span key={index} className="algorithm-tag">{tag}</span>
          ))}
        </div>
      </div>
    </Link>
  );
}

export default AlgorithmCard;
