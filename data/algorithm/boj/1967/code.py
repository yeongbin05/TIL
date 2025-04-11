import sys
input = sys.stdin.readline
from collections import defaultdict, deque

# 트리 정보를 입력받고, 그래프를 만듭니다.
n = int(input())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

# 가장 먼 노드와 그 거리를 반환하는 함수입니다.
def bfs(start):
    distance = [-1] * (n + 1)  # 각 노드까지의 거리를 저장합니다.
    distance[start] = 0
    queue = deque([start])
    farthest_node = start  # 가장 먼 노드를 저장할 변수입니다.
    
    while queue:
        node = queue.popleft()
        
        for neighbor, weight in graph[node]:
            if distance[neighbor] == -1:  # 방문하지 않은 노드만 처리
                distance[neighbor] = distance[node] + weight
                queue.append(neighbor)
                
                # 현재 노드까지의 거리가 가장 크다면, 업데이트
                if distance[neighbor] > distance[farthest_node]:
                    farthest_node = neighbor
    
    return farthest_node, distance[farthest_node]

# 첫 번째 BFS를 실행하여 가장 먼 노드를 찾습니다.
farthest_node, _ = bfs(1)

# 두 번째 BFS를 실행하여 지름을 계산합니다.
_, diameter = bfs(farthest_node)

print(diameter)
