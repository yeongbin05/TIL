import os
import re

# ✅ 태그 매핑 (필요시 추가 가능)
TAG_MAPPING = {
    "1차원 배열": "Array",
    "2차원 배열": "Matrix",
    "해시를 사용한 집합과 맵": "Hash Table",
    "자료 구조": None,
    "자료 구조 일반": None,
    "수학": "Math",
    "정수론": "Number Theory",
    "조합론": "Combinatorics",
    "소수 판정": "Math",
    "확률론": "Probability and Statistics",
    "기하학": "Geometry",
    "브루트포스 알고리즘": "Brainteaser",
    "백트래킹": "Backtracking",
    "재귀": "Recursion",
    "비트마스킹": "Bitmask",
    "문자열": "String",
    "문자열 처리": "String",
    "파싱": "String Matching",
    "트라이": "Trie",
    "정규 표현식": "String Matching",
    "누적 합": "Prefix Sum",
    "투 포인터": "Two Pointers",
    "슬라이딩 윈도우": "Sliding Window",
    "스택": "Stack",
    "큐": "Queue",
    "덱": "Queue",
    "우선순위 큐": "Heap (Priority Queue)",
    "스택을 사용한 구현": "Monotonic Stack",
    "자료형": None,
    "연결 리스트": "Linked List",
    "이중 연결 리스트": "Doubly-Linked List",
    "그래프 이론": "Graph",
    "그래프 탐색": "Graph",
    "깊이 우선 탐색": "Depth-First Search",
    "너비 우선 탐색": "Breadth-First Search",
    "최단 경로": "Shortest Path",
    "다익스트라": "Shortest Path",
    "벨만-포드": "Shortest Path",
    "플로이드-워셜": "Shortest Path",
    "위상 정렬": "Topological Sort",
    "강한 연결 요소": "Strongly Connected Component",
    "이분 그래프": "Graph",
    "트리": "Tree",
    "이진 트리": "Binary Tree",
    "이진 탐색 트리": "Binary Search Tree",
    "세그먼트 트리": "Segment Tree",
    "펜윅 트리": "Binary Indexed Tree",
    "LCA": "Tree",
    "트리에서의 동적 계획법": "Dynamic Programming",
    "그래프에서의 최단 경로": "Shortest Path",
    "MST": "Minimum Spanning Tree",
    "유니온 파인드": "Union Find",
    "DFS": "Depth-First Search",
    "BFS": "Breadth-First Search",
    "다이나믹 프로그래밍": "Dynamic Programming",
    "메모이제이션": "Memoization",
    "분할 정복": "Divide and Conquer",
    "탐색": "Binary Search",
    "이분 탐색": "Binary Search",
    "삼분 탐색": "Binary Search",
    "정렬": "Sorting",
    "병합 정렬": "Merge Sort",
    "퀵 정렬": "Quickselect",
    "카운팅 정렬": "Counting Sort",
    "버블 정렬": "Sorting",
    "삽입 정렬": "Sorting",
    "선택 정렬": "Sorting",
    "기수 정렬": "Radix Sort",
    "버킷 정렬": "Bucket Sort",
    "셸 정렬": "Shell",
    "슬라이딩 윈도우": "Sliding Window",
    "그리디 알고리즘": "Greedy",
    "이분 매칭": "Graph",
    "네트워크 플로우": "Graph",
    "에라토스테네스의 체": "Number Theory",
    "투 포인터 알고리즘": "Two Pointers",
    "KMP": "String Matching",
    "Rolling Hash": "Rolling Hash",
    "라빈-카프": "Rolling Hash",
    "문자열 해싱": "Hash Function",
    "조합": "Combinatorics",
    "부분 수열": "Prefix Sum",
    "부분 배열": "Prefix Sum",
    "문자열 압축": "String",
    "문자열 분리": "String Matching",
    "정렬된 배열": "Array",
    "정렬된 리스트": "Array",
    "트리 순회": "Tree",
    "힙": "Heap (Priority Queue)",
    "단조 스택": "Monotonic Stack",
    "단조 큐": "Monotonic Queue",
    "최소 공통 조상": "Tree",
    "탐욕법": "Greedy",
    "시뮬레이션": "Simulation",
    "구현": "Design",
    "상태 공간 탐색": "Backtracking",
    "게임 이론": "Game Theory",
    "인터랙티브": "Interactive",
    "데이터 스트림": "Data Stream",
    "정렬된 집합": "Ordered Set",
    "이터레이터": "Iterator",
    "동시성": "Concurrency",
    "랜덤화 알고리즘": "Randomized",
    "저장 샘플링": "Reservoir Sampling",
    "강한 결합 요소": "Strongly Connected Component",
    "라인 스위핑": "Line Sweep",
    "에디토리얼": None,
    "비공식 알고리즘": None,
}

UNMAPPED_TAGS = {}

BASE_PATH = "public/data/algorithm/boj/"

def convert_tags(original_tags, problem_id):
    new_tags = []
    for tag in original_tags:
        mapped = TAG_MAPPING.get(tag)
        if mapped:
            new_tags.append(mapped)
        elif mapped is None:
            continue  # 의미 없는 분류 제거
        else:
            # 매핑 안 된 태그 저장
            if problem_id not in UNMAPPED_TAGS:
                UNMAPPED_TAGS[problem_id] = []
            UNMAPPED_TAGS[problem_id].append(tag)
    return new_tags

def process_problem_folder(folder_name):
    problem_path = os.path.join(BASE_PATH, folder_name)
    md_path = os.path.join(problem_path, "description.md")

    if not os.path.isfile(md_path):
        return

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line.startswith("tags:") or line.startswith("태그:"):
            # 태그 추출
            tag_str = line.split(":", 1)[1].strip()
            original_tags = [tag.strip() for tag in tag_str.split(",") if tag.strip()]
            converted = convert_tags(original_tags, folder_name)
            new_line = f"tags: {', '.join(converted)}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(md_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

def main():
    for folder in os.listdir(BASE_PATH):
        if os.path.isdir(os.path.join(BASE_PATH, folder)):
            process_problem_folder(folder)

    print("\n\n🔎 매핑되지 않은 태그:")
    for problem_id, tags in UNMAPPED_TAGS.items():
        print(f"{problem_id}: {tags}")

if __name__ == "__main__":
    main()
