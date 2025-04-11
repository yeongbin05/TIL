def dfs(num):
    global cnt
    cnt += 1
    visited[num] = True
    for i in nodes[num]:
        if visited[i] == False:
            dfs(i)
    return cnt - 1
n = int(input())
m = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    nodes[x].append(y)
    nodes[y].append(x)
visited = [False] * (n+1)
cnt = 0
print(dfs(1))
