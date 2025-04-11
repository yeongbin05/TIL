from collections import deque
import sys
input = sys.stdin.readline
def find_path(row,col):
    q = deque([(row,col)])
    while q :
        ci,cj = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<m and map[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if map[i][j] == 2 :
            find_path(i,j)

for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for i in visited:
    print(*i)