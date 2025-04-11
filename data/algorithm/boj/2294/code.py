from collections import deque


def bfs(start):
    q = deque([start])

    while q:
        current = q.popleft()
        if current == k:
            return
        for i in coins:
            next = current + i
            if 0 <= next < 10001 and visited[next] == 0:
                q.append(next)
                visited[next] = visited[current] + 1


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
visited = [0 for _ in range(10001)]
bfs(0)
if visited[k] == 0:
    print(-1)
else:
    print(visited[k])
