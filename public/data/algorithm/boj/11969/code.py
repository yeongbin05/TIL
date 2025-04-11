import sys
input = sys.stdin.readline
n,q = map(int,input().split())
prefix = [[0,0,0] for _ in range(n+1)]
for i in range(1,n+1):
    x = int(input())
    prefix[i] = prefix[i-1][:]
    prefix[i][x-1] += 1

for j in range(q):
    x,y = map(int,input().split())
    
    a = prefix[y]
    b = prefix[x-1]
    result = [c - d for c, d in zip(a, b)]
    print(*result)