from  collections import deque

def bfs(row,col):
    q = deque([(row,col)])
    visited[row][col] = 1
    while q :
        ci,cj = q.popleft()
        if ci == n-1 and cj ==  m-1:
            return visited[ci][cj]
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and map[ni][nj] == 1:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1




n,m = map(int,input().split())
map = [list(map(int,input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(bfs(0,0))