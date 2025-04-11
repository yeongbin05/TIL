import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [0] + list(map(int,input().split()))
prefix = [0] * (n+1)
for i in range(1,n+1):
    prefix[i] = prefix[i-1] + A[i]
for _ in range(m):
    x,y = map(int,input().split())
    print(prefix[y] - prefix[x-1])