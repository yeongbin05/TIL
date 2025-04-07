import React from 'react';
import './Header.css';
import { Link } from 'react-router-dom';

function Header() {
  // 클릭 시 해당 섹션으로 스크롤 이동하는 함수
  const handleScroll = (e, sectionId) => {
    e.preventDefault();
    const section = document.querySelector(sectionId);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className="site-header" id="header">
      <div className="container">
        <div className="logo">내 포트폴리오</div>
        <nav className="main-nav">
          <ul>
            <li><a href="#hero" onClick={(e) => handleScroll(e, '#hero')}>홈</a></li>
            <li><a href="#about" onClick={(e) => handleScroll(e, '#about')}>소개</a></li>
            <li><a href="#projects" onClick={(e) => handleScroll(e, '#projects')}>프로젝트</a></li>

            {/* ✅ 여기 수정됨 */}
            <li className="study-menu">
              <span className="study-toggle">스터디 ▼</span>
              <ul className="dropdown">
              <li><Link to="/algorithm">알고리즘</Link></li>
                <li><a href="#study-resources" onClick={(e) => handleScroll(e, '#study-resources')}>CS</a></li>
              </ul>
            </li>

            <li><a href="#contact" onClick={(e) => handleScroll(e, '#contact')}>연락처</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
