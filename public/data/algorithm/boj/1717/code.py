import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    print(parent,'find')
    return parent[x]

def union(x,y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if rootX > rootY :
            parent[rootX] = rootY

        elif rootX < rootY :
            parent[rootY] = rootX
    print(parent,'union')
n,m = map(int,input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    x,a,b = map(int,input().split())
    if x == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')