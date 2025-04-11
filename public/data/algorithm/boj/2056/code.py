from collections import deque
import sys
input = sys.stdin.readline

def solve():
    # 입력 처리
    n = int(input().strip())  # 작업의 수
    graph = [[] for _ in range(n + 1)]  # 작업의 선행 관계를 저장하는 그래프
    in_degree = [0] * (n + 1)  # 각 작업의 진입 차수
    times = [0] * (n + 1)  # 각 작업의 수행 시간
    dp = [0] * (n + 1)  # 각 작업이 완료되는 데 걸리는 최소 시간

    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        time = data[0]  # 작업 i의 수행 시간
        times[i] = time
        for prerequisite in data[2:]:
            graph[prerequisite].append(i)  # 선행 관계 저장
            in_degree[i] += 1  # 진입 차수 증가

    # 위상 정렬 수행
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:  # 선행 관계가 없는 작업을 큐에 추가
            q.append(i)
            dp[i] = times[i]  # 초기 작업의 최소 시간 설정
    print(graph)
    while q:
        current = q.popleft()
        for next_task in graph[current]:
            in_degree[next_task] -= 1
            dp[next_task] = max(dp[next_task], dp[current] + times[next_task])  # 최소 시간 갱신
            if in_degree[next_task] == 0:
                q.append(next_task)

    # 결과 출력
    print(max(dp))

solve()
