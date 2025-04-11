# https://www.acmicpc.net/problem/2252
from collections import deque
import sys 
input = sys.stdin.readline
n,m = map(int,input().split())
nodes = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

# 방향 그래프 구성 및 진입 차수 계산
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1,n+1):
    if in_degree[i] == 0:
        q.append(i)
ans = []
while q :
    start = q.popleft()
    print(start,end=" ")
    for next_node in nodes[start]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)
