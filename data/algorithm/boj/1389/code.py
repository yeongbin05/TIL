from collections import deque
import sys
input = sys.stdin.readline
def bfs(start,cnt):
    q = deque([(start,cnt)])
    visited[start] = cnt 
    while q :
        
        a = q.popleft()
        for i in friend[a[0]]:
            if visited[i] == -1:
                visited[i] = a[1] + 1
                q.append((i,a[1]+1))
n,m = map(int,input().split())
friend = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
ans_visited = float('inf')
ans = 0
for i in range(1,n+1):
    visited = [-1 for _ in range(n+1)]
    bfs(i,0)
    # print(visited)
    temp = sum(visited)
    if temp < ans_visited :
        ans_visited = temp
        ans = i
    
print(ans)