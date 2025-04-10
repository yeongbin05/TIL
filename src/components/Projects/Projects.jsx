import React, { useState } from 'react';
import './Projects.css';
import Modal from '../Modal/Modal';

const projectList = [
  {
    id: 1,
    title: '유저와 아티스트를 잇는 실시간 스트리밍 서비스',
    description: '실시간 방송 플랫폼의 백엔드 구축',
    thumbnail: 'images/ving-mockup.PNG'
  },
  {
    id: 2,
    title: '맞춤형 음식 추천 시스템',
    description: '사용자 데이터를 바탕으로 식단을 추천',
    
    thumbnail: 'images/mozzi-thumbnail.PNG'
  }
];

function Projects() {
  const [selectedProjectId, setSelectedProjectId] = useState(null);

  const openModal = (id) => setSelectedProjectId(id);
  const closeModal = () => setSelectedProjectId(null);

  return (
    <section className="projects section" id="projects">
      <div className="container">
        <h2>Projects</h2>
        <div className="project-list">
          {projectList.map((project) => (
            <div
              className="project-item"
              key={project.id}
              onClick={() => openModal(project.id)}
            >
              <img src={project.thumbnail} alt={project.title} />
              <h3>{project.title}</h3>
              <p>{project.description}</p>
            </div>
          ))}
        </div>
        <Modal
          isOpen={!!selectedProjectId}
          onClose={closeModal}
          projectId={selectedProjectId}
        />
      </div>
    </section>
  );
}

export default Projects;
