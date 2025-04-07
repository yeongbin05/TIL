import React from 'react';
import './Hero.css';

function Hero() {
  return (
    <section id="home" className="hero">
      <div className="container">
        <h1>안녕하세요, 개발자 김영빈입니다.</h1>
        <a href="#projects" className="btn">프로젝트 보기</a>
      </div>
    </section>
  );
}

export default Hero;
