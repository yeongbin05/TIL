from collections import deque
import sys
input = sys.stdin.readline
def bfs(s_i,s_j):
    q = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                q.append((i,j,'w'))
    q.append((s_i,s_j,'s'))
    while q :
        ci,cj,x = q.popleft()
        if x == 's' and ci == d_i and cj == d_j:
            return
        
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = ci + di , cj + dj
            if 0<=ni<r and 0<=nj<c and (board[ni][nj] == '.' or board[ni][nj] == 'D') and not visited[ni][nj] :
                if x == 's':
                    
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni,nj,x))
                else:
                    if board[ni][nj] != 'D':
                        visited[ni][nj] = True
                        q.append((ni,nj,x))

r,c = map(int,input().split())
board = [input() for _ in range(r)]
visited = [[0] * c for _ in range(r)]
d_i,d_j = 0,0
s_i,s_j = 0,0
#물 위치
for i in range(r):
    for j in range(c):
        if board[i][j] == 'D':
            d_i,d_j = i,j
        if board[i][j] == 'S':
            s_i,s_j = i,j
        

bfs(s_i,s_j)

# for i in visited:
#     print(i)
if visited[d_i][d_j] == 0:
    print('KAKTUS')
else:
    print(visited[d_i][d_j])