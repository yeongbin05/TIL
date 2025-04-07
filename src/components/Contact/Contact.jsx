import React from 'react';
import './Contact.css';

function Contact() {
  return (
    <>
      <section id="contact" className="section contact">
        <div className="container">
          <h2>어학</h2>
          <p>TOEIC : 915 </p>
          <p>TOEIC SPEAKING : AL </p>
          <p>JLPT : 一級 </p>
          <p>JPT : 825 </p>
        </div>
      </section>

      <section id="contact" className="section contact">
        <div className="container">
          <h2>연락처</h2>
          <p>Email: bigstar96115@hanmail.net</p>
          <p>GitHub: <a href="https://github.com/yeongbin05" target="_blank">github.com/yeongbin05</a></p>
        </div>
      </section>
    </>
  );
}

export default Contact;