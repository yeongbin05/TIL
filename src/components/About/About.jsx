import React from 'react';
import './About.css';

function About() {
  return (
    <section id="about" className="section about">
      <div className="container">
        <h2>소개</h2>
        <p>
          SSAFY(삼성 소프트웨어 아카데미)에서 시작해 Django 기반 프로젝트를 통해 AWS, Git, Notion을 활용한 협업 경험을 쌓았습니다. <br />
          영상 관련 기술과 대용량 트래픽 처리에 관심이 많으며, 백엔드 개발자로서 새로운 기술을 배우는 것에도 열려있습니다.<br />
          알고리즘 문제 해결과 개인프로젝트 및 CS 지식을 바탕으로 지속적으로 성장하고 있으며, 도전적인 과제를 통해 성과를 이루고자 합니다.
        </p>
      </div>
    </section>
  );
}

export default About;
