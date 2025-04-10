import React from 'react';
import './Header.css';
import { Link, useLocation } from 'react-router-dom';

function Header() {
  const location = useLocation();
  const isHome = location.pathname === '/';

  const handleScroll = (e, sectionId) => {
    e.preventDefault();
    if (isHome) {
      const section = document.querySelector(sectionId);
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
      }
    }
  };

  return (
    <header className="site-header" id="header">
      <div className="container">
        <div className="logo">내 포트폴리오</div>
        <nav className="main-nav">
          <ul>
            <li>
              {isHome ? (
                <a href="#hero" onClick={(e) => handleScroll(e, '#hero')}>홈</a>
              ) : (
                <Link to="/#hero">홈</Link>
              )}
            </li>
            <li>
              {isHome ? (
                <a href="#about" onClick={(e) => handleScroll(e, '#about')}>소개</a>
              ) : (
                <Link to="/#about">소개</Link>
              )}
            </li>
            <li>
              {isHome ? (
                <a href="#projects" onClick={(e) => handleScroll(e, '#projects')}>프로젝트</a>
              ) : (
                <Link to="/#projects">프로젝트</Link>
              )}
            </li>

            <li className="study-menu">
              <span className="study-toggle">스터디 ▼</span>
              <ul className="dropdown">
                <li>
                  <Link to="/algorithm">알고리즘</Link>
                </li>
                <li>
                  <Link to="/cs">CS</Link>
                </li>
              </ul>
            </li>

            <li>
              {isHome ? (
                <a href="#contact" onClick={(e) => handleScroll(e, '#contact')}>연락처</a>
              ) : (
                <Link to="/#contact">연락처</Link>
              )}
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
