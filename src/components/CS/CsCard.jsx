import React from 'react';
import './CsCard.css';
import { Link } from 'react-router-dom';

function CsCard({ data }) {
  const { id,title, description, tags, thumbnail } = data;
  const truncate = (text, maxLength) => {
    if (!text) return '';
    return text.length > maxLength ? text.slice(0, maxLength) + '...' : text;
  };
  return (
    <Link to={`/cs/${id}`} className="algorithm-card-link">
    <div className="cs-card">
      {/* {thumbnail && (
        <img
          className="cs-card-thumbnail"
          src={thumbnail}
          alt={title}
        />
      )} */}
      <h3>{title}</h3>
      <p>{truncate(description, 100)}</p>


      <div className="cs-tags">
        {tags.map((tag, idx) => (
          <span key={idx} className="cs-tag">
            {tag}
          </span>
        ))}
      </div>
    </div>
    </Link>
  );
}

export default CsCard;
