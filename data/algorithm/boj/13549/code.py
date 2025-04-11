# https://www.acmicpc.net/problem/13549
from collections import deque

def bfs(start,cnt):
    q = deque([(start,cnt)])
    visited[start] = cnt 
    while q:
        c,cnt = q.popleft()
        if c == m:
            return 
        if 0 <= 2*c <= 200000 and visited[2*c] > cnt:
            visited[2*c] = cnt
            q.appendleft((2*c, cnt)) 

        for i in (1, -1):
            if 0 <= c + i <= 200000 and visited[c + i] > cnt + 1:
                visited[c + i] = cnt + 1
                q.append((c + i, cnt + 1))
        
n,m = map(int,input().split())
visited = [float('inf')] * 200001
cnt = 0
bfs(n,cnt)

print(visited[m])