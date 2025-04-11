from collections import deque
import sys

input = sys.stdin.readline


def bfs(node):
    q = deque([node])
    visited[node] = True

    while q:
        parent = q.popleft()
        for i in nodes[parent]:
            if not visited[i]:
                parents[i] = parent
                q.append(i)
                visited[i] = True


n = int(input())
nodes = [[] for _ in range(n + 1)]
for i in range(n - 1):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)

parents = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

bfs(1)

for i in range(2, n + 1):
    print(parents[i])
