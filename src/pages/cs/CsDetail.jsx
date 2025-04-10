import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Header from '../../components/Header/Header';
import ReactMarkdown from 'react-markdown';  // 마크다운 렌더링을 위한 라이브러리
import './CsDetail.css';  // 스타일 파일

function CSDetail() {
  const { id } = useParams();  // URL에서 id 가져오기
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [isLoading, setIsLoading] = useState(true);  // 로딩 상태 관리

  useEffect(() => {
    // id에서 '-'를 제거하고, 실제 md 파일명으로 변환
    const folderName = id.split('-')[0];  // 'os-os1' => 'os1'
    const fileName = id.split('-')[1];  // 'os-os1' => 'os1'
    fetch(`${process.env.PUBLIC_URL}/data/cs/${folderName}/${fileName}.md`)
      .then((res) => {
        if (!res.ok) {
          throw new Error('파일을 불러오지 못했습니다.');
        }
        return res.text();
      })
      .then((text) => {
        setContent(text);  // 파일 내용을 설정
        setIsLoading(false);  // 로딩 종료
      })
      .catch((error) => {
        setContent('📄 내용을 불러오지 못했습니다.');  // 에러 발생 시 내용 설정
        setIsLoading(false);  // 로딩 종료
        console.error('Error loading file:', error);  // 에러 로그 출력
      });
  }, [id]);

  useEffect(() => {
    // cs.json에서 title 가져오기
    fetch(`${process.env.PUBLIC_URL}/data/cs/cs.json`)
      .then((res) => res.json())
      .then((data) => {
        const matched = data.find((item) => item.id === id);
        if (matched) setTitle(matched.title);
      });
  }, [id]);

  if (isLoading) {
    return <div>로딩 중...</div>;  // 로딩 중일 때 표시할 내용
  }

  return (
    <div className="cs-detail-wrapper">
      <Header />
      <div className="cs-detail-content">
        <h2 className="cs-title">📚 {title}</h2>
        
        {/* ReactMarkdown 사용하여 md 내용 렌더링 */}
        <div className="cs-description">
          <ReactMarkdown
            children={content}
            components={{
              img: ({ node, ...props }) => (
                <img
                  {...props}
                  src={`${process.env.PUBLIC_URL}/data/cs/${id.split('-')[1]}/${props.src}`}
                  alt={props.alt}
                  className="cs-image"
                />
              ),
            }}
          />
        </div>
      </div>
    </div>
  );
}

export default CSDetail;
