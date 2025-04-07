import React from "react";
import { useParams } from "react-router-dom";
import "./AlgorithmDetail.css";

function AlgorithmDetail() {
  const { id } = useParams();

  return (
    <div className="algorithm-detail">
      <h1>알고리즘 상세 페이지</h1>
      <p>선택한 알고리즘 ID: {id}</p>
      {/* 여기에 알고리즘 설명 & 코드 추가 */}
    </div>
  );
}

export default AlgorithmDetail;
