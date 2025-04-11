from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        node = q.popleft()
        for i in vertex[node]:
            if not visited[i] :
                visited[i] = True
                q.append(i)

n,m = map(int,input().split())
vertex = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    vertex[x].append(y)
    vertex[y].append(x)
ans = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)

