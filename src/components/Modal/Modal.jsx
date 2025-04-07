import React from 'react';
import './Modal.css';

const projectDetails = {
  1: {
    title: '프로젝트 1: 유저와 아티스트를 잇는 실시간 스트리밍 서비스',
    description: '아티스트의 실시간 방송을 시청할 수 있는 서비스 백엔드를 구축하였습니다.',
    features: [
      '실시간 방송 스트리밍',
      '채팅 기능',
      'Adaptive Bitrate Streaming'
    ],
    Role: [
      'DB 및 서비스 설계',
      'nginx-rtmp를 이용한 미디어 서버 구축',
      'Django를 이용한 API 개발',
      '스트리밍된 영상을 실시간으로 처리하여 S3에 업로드',
      'Cloudfront를 이용한 정적 파일 CDN 구현'
    ],
    techStack: [
      'Backend: Django',
      'Database: MySQL, MongoDB', 
      'DevOps: Docker'
    ],
    erdImage: 'images/ving_erd.webp',
    architectureImage: 'images/ving-architecture.PNG'
  },
  2: {
    title: '프로젝트 2: 맞춤형 음식 추천 시스템',
    description: '사용자의 식습관, 알러지 정보, 냉장고 식재료 데이터를 활용하여 맞춤형 음식 추천을 제공하는 백엔드 시스템을 구축하였습니다.',
    features: [
      '사용자별 음식 및 식재료 선호도 분석',
      '냉장고 보유 식재료 기반 추천 알고리즘 적용',
      'RDBMS를 활용한 음식-사용자 관계 데이터 관리'
    ],
    Role: [
      'DB 및 API 설계',
      '공공 API에서 받은 데이터를 전처리',
      '추천 알고리즘 개발',
      'Django를 이용한 API 개발'
    ],
    techStack: [
      'Backend: Django',
      'Database: MySQL, MongoDB',
      'Streaming & Storage: Nginx RTMP, Docker, AWS S3',
      'Algorithm: 사용자 데이터 기반 추천 알고리즘'
    ],
    erdImage: 'images/ving_erd.webp',
    architectureImage: 'images/ving_architecture.PNG'
  }
};

function Modal({ isOpen, onClose, projectId }) {
  if (!isOpen) return null;

  const details = projectDetails[projectId];
  if (!details) return null;

  return (
    <div className="modal" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <span className="close-btn" onClick={onClose}>&times;</span>
        <div className="modal-body">
          <h3>{details.title}</h3>
          <p><strong>설명:</strong> {details.description}</p>

          <h4>📌 주요 기능</h4>
          <ul className="ul-margin">
            {details.features.map((f, i) => <li key={i}>{f}</li>)}
          </ul>

          <h4>📌 기술 스택</h4>
          <ul className="ul-margin">
            {details.techStack.map((t, i) => <li key={i}><strong>{t}</strong></li>)}
          </ul>

          <h4>📌 ERD</h4>
          <img src={details.erdImage} alt={details.title} className="modal-project-image" />

          <h4>📌 아키텍처</h4>
          <img src={details.architectureImage} alt={details.title} className="modal-project-image" />

          <h4>📌 협업 노션</h4>
          <a
            href="https://grizzled-lord-170.notion.site/1d7e7e3ccb5d4b5e973ab53cb9cef05a"
            target="_blank"
            rel="noreferrer"
            style={{ marginLeft: '25px' }}
          >
            Notion Link
          </a>
        </div>
      </div>
    </div>
  );
}

export default Modal;
