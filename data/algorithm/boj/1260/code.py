from collections import deque
import sys
input = sys.stdin.readline
def dfs(start):
    visited[start] = True
    print(start,end=" ")
    for i in vertex[start]:
        if not visited[i]:
            dfs(i)
def bfs(start):
    visited[start] = True
    q = deque([start])
    
   
    while q:
        i = q.popleft()
        
        visited[i] = True
    
        print(i,end=" ")
        for j in vertex[i]:
            if not visited[j]:
                q.append(j)
                visited[j] = True
             
        
n,m,v = map(int,input().split())
vertex = [[] for _ in range(n+1)]
visited = [ False for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    vertex[a].append(b)
    vertex[b].append(a)
for i in vertex:
    i.sort()
dfs(v)
print()
visited = [ False for _ in range(n+1)]

bfs(v)