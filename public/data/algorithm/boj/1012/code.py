from collections import deque
import sys
input = sys.stdin.readline
def bfs(row,col):
    visited[row][col] = 1
    q = deque([(row,col)])
    while q:
        di,dj = q.popleft()
        for ci,cj in ((1,0),(-1,0),(0,1),(0,-1)) :
            ni = ci + di
            nj = cj + dj
            if 0<=ni<n and 0<=nj<m and board[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = 1
                
    
        
t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    board = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(k):
        x,y = map(int,input().split())
        board[y][x] = 1

    for j in range(n):
        for k in range(m):
            if board[j][k] == 1 and not visited[j][k]:
                bfs(j,k)
                cnt += 1
    print(cnt)