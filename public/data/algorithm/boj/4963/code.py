from collections import deque
import sys
input = sys.stdin.readline
def bfs(board,row,col):
    q = deque([(row,col)])
    visited[row][col] = True
    while q :
        ci,cj = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<m and 0<=nj<n and board[ni][nj] == 1 and visited[ni][nj] == False:
                q.append((ni,nj))
                visited[ni][nj] = True
while 1 :
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break

    board = [list(map(int,input().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1 and not visited[i][j] :
                bfs(board,i,j)
                ans += 1

    print(ans)