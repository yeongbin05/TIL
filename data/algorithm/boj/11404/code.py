import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

INF = float('inf')
connect = [[INF] * n for _ in range(n)]


for _ in range(m):
    a, b, cost = map(int, input().split())
    connect[a-1][b-1] = min(connect[a-1][b-1],cost)
for i in range(n):
    connect[i][i] = 0
for k in range(n):
    for a in range(n):
        for b in range(n):
            connect[a][b] = min(connect[a][b],connect[a][k]+connect[k][b])

for i in range(n):
    for j in range(n):
        # 갈 수 없는 경우 0으로 출력
        if connect[i][j] == INF:
            print(0, end=" ")
        else:
            print(connect[i][j], end=" ")
    print()