from collections import deque


def bfs(row, col):
    q = deque([(row, col, k)])  # (행, 열, 남은 말 이동 횟수)
    visited[row][col][k] = 0  # 시작점의 방문 처리, 남은 말 이동 횟수도 포함

    while q:
        ci, cj, remaining_k = q.popleft()

        # 목적지에 도달하면 이동한 횟수 반환
        if ci == h - 1 and cj == w - 1:
            return visited[ci][cj][remaining_k]

        # 말처럼 이동할 수 있는 경우
        if remaining_k > 0:
            for di, dj in (
                (-2, -1),
                (-1, -2),
                (1, -2),
                (2, -1),
                (2, 1),
                (1, 2),
                (-1, 2),
                (-2, 1),
            ):
                ni, nj = ci + di, cj + dj
                if (
                    0 <= ni < h
                    and 0 <= nj < w
                    and visited[ni][nj][remaining_k - 1]
                    == -1  # 말처럼 이동 시 남은 말 이동 횟수를 줄임
                    and board[ni][nj] == 0  # 장애물이 없어야 이동 가능
                ):
                    q.append((ni, nj, remaining_k - 1))
                    visited[ni][nj][remaining_k - 1] = visited[ci][cj][remaining_k] + 1

        # 일반 이동 (상하좌우)
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if (
                0 <= ni < h
                and 0 <= nj < w
                and visited[ni][nj][remaining_k] == -1  # 말 이동 횟수는 유지됨
                and board[ni][nj] == 0  # 장애물이 없어야 이동 가능
            ):
                q.append((ni, nj, remaining_k))
                visited[ni][nj][remaining_k] = visited[ci][cj][remaining_k] + 1

    return None  # 도달할 수 없는 경우


# 입력 처리
k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
visited = [
    [[-1] * (k + 1) for _ in range(w)] for _ in range(h)
]  # 말 이동 횟수까지 고려한 방문 배열

# BFS 실행
ans = bfs(0, 0)

# 결과 출력
if ans is None:
    print(-1)
else:
    print(ans)
