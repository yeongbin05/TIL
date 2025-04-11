from collections import deque
import sys
input = sys.stdin.readline
def bfs(rain,row,col):
    q = deque([(row,col)])
    visited[row][col] = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0 and board[ni][nj] > rain :
                q.append((ni,nj))
                visited[ni][nj] = 1 
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

Min,Max = float('inf'),0
# ans 0 으로 시작하려면 rain을 0부터 Max까지 해야하고
# rain을 Min부터 시작하고 싶으면 ans 를 1부터하면됨
ans = 0
for i in range(n):
    for j in range(n):
        if board[i][j] < Min :
            Min = board[i][j]

        if board[i][j] > Max :
            Max = board[i][j]

for i in range(Max):
    temp = 0
    visited = [[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and board[j][k] > i:
                bfs(i,j,k)
                temp += 1
                
    if temp > ans:
        ans = temp

print(ans)