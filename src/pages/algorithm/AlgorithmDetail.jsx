// pages/algorithm/AlgorithmDetail.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Header from '../../components/Header/Header';
import ReactMarkdown from 'react-markdown';  // 마크다운 렌더링을 위한 라이브러리
import './AlgorithmDetail.css';

function AlgorithmDetail() {
  const { id } = useParams();
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [code, setCode] = useState('');

  useEffect(() => {
    // description.md 불러오기
    const folderName = id.replace(/-/g, '_');
    fetch(`${process.env.PUBLIC_URL}/data/algorithm/${folderName}/description.md`)
      .then((res) => res.text())
      .then(setDescription)
      .catch(() => setDescription('📄 설명을 불러오지 못했습니다.'));

    // solution.py 불러오기
    fetch(`${process.env.PUBLIC_URL}/data/algorithm/${folderName}/code.py`)
      .then((res) => res.text())
      .then(setCode)
      .catch(() => setCode('# ❌ 코드 불러오기 실패'));
  }, [id]);

  useEffect(() => {
    // index.json에서 title만 가져오기
    fetch(`${process.env.PUBLIC_URL}/data/algorithm/index.json`)
      .then((res) => res.json())
      .then((data) => {
        const matched = data.find((item) => item.id === id);
        if (matched) setTitle(matched.title);
      });
  }, [id]);

  return (
    <div className="algorithm-detail-wrapper">
      <Header />
      <div className="algorithm-detail-content">
        <h2 className="algorithm-title">🧩 {title}</h2>
        
        {/* ReactMarkdown 사용하여 description 마크다운 렌더링 */}
        <div className="algorithm-description">
          <ReactMarkdown
            children={description}
            components={{
              img: ({ node, ...props }) => (
                <img
                  {...props}
                  src={`${process.env.PUBLIC_URL}/data/algorithm/${id.replace(/-/g, '_')}/${props.src}`}
                  alt={props.alt}
                  className="algorithm-image"
                />
              )
            }}
          />
        </div>
        
        <h3 className="algorithm-title">💻 풀이 코드</h3>
        <pre style={{padding: '1rem', color: '#0f0', overflowX: 'auto' }}>
          {code}
        </pre>
      </div>
    </div>
  );
}

export default AlgorithmDetail;
