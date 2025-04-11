from collections import deque
def bfs(row,col):
    q = deque([(row,col)])
    visited[row][col] = 1
    temp = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni< n and 0<=nj<n and visited[ni][nj] == 0 and board[ni][nj] == 1:
                q.append((ni,nj))
                visited[ni][nj] = 1
                temp += 1
    return temp
n = int(input())
board = [list(map(int,input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i,j))
            cnt += 1
print(cnt)
for i in sorted(ans):
    print(i)