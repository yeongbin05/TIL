from collections import deque
import sys
input = sys.stdin.readline

def solve():
    # 입력 처리
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)]  # 선수 조건 그래프
    in_degree = [0] * (n + 1)  # 진입 차수 배열
    semester = [0] * (n + 1)  # 최소 학기 저장 배열

    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        in_degree[b] += 1

    # 위상 정렬 준비
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            semester[i] = 1  # 선수 과목이 없으므로 1학기에 수강 가능

    # 위상 정렬 수행
    while q:
        current = q.popleft()
        for neighbor in edges[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
                semester[neighbor] = semester[current] + 1  # 현재 과목 학기 + 1

    # 결과 출력
    print(' '.join(map(str, semester[1:])))

solve()
