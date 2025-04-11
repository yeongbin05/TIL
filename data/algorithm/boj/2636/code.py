from collections import deque
import sys
input = sys.stdin.readline
 
r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
melt_history = [] # 녹인 치즈의 개수를 저장할 리스트
time = 0 
 
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cnt = 0
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                if board[nx][ny] == 1: # 인접한 곳이 치즈라면 녹인다.
                    board[nx][ny] = 0
                    cnt += 1
                visited[nx][ny] = True
    melt_history.append(cnt)
    return cnt
 
while True:
    visited = [[False] * c for _ in range(r)]
 
    melt_cnt = bfs()
 
    if melt_cnt == 0: # 녹일 수 있는 치즈가 없다면
        print(time)
        print(melt_history[-2])
        break
    time += 1