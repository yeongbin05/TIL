import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./AlgorithmList.css";

const dummyData = [
  { id: 1, title: "이진 탐색", description: "정렬된 배열에서 빠르게 찾기", thumbnail: "/images/binary-search.jpg" },
  { id: 2, title: "다익스트라", description: "최단 경로 탐색", thumbnail: "/images/dijkstra.jpg" },
  { id: 3, title: "퀵 정렬", description: "빠른 정렬 알고리즘", thumbnail: "/images/quick-sort.jpg" },
  { id: 4, title: "머지 정렬", description: "안정적인 정렬 제공", thumbnail: "/images/merge-sort.jpg" },
  { id: 5, title: "DFS / BFS", description: "그래프 탐색 알고리즘", thumbnail: "/images/dfs-bfs.jpg" },
  { id: 6, title: "유클리드 호제법", description: "최대공약수(GCD) 계산", thumbnail: "/images/euclid.jpg" },
  { id: 7, title: "KMP 알고리즘", description: "문자열 검색 최적화", thumbnail: "/images/kmp.jpg" },
  { id: 8, title: "플로이드-워셜", description: "모든 정점 간 최단 경로", thumbnail: "/images/floyd.jpg" },
  { id: 9, title: "투 포인터", description: "배열 문제 최적화", thumbnail: "/images/two-pointer.jpg" },
  { id: 10, title: "세그먼트 트리", description: "빠른 구간 합 구하기", thumbnail: "/images/segment-tree.jpg" },
];

function AlgorithmList() {
  const [algorithms] = useState(dummyData.slice(0, 5)); // 최대 5개만 가져오기

  return (
    <div className="algorithm-list">
      <h1>📌 알고리즘 목록</h1>
      <div className="algorithm-container">
        {algorithms.map((algo) => (
          <Link to={`/algorithm/${algo.id}`} key={algo.id} className="algorithm-card">
            <img src={algo.thumbnail} alt={algo.title} />
            <div className="algorithm-info">
              <h2>{algo.title}</h2>
              <p>{algo.description}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default AlgorithmList;
