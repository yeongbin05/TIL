import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
prefix = [0] * (n+1)
A = [0] + A
prefix[1] = A[1]
for i in range(2,n+1):
    prefix[i] = prefix[i-1] + A[i]
m = int(input())


for _ in range(m):
    x,y = map(int,input().split())
    print(prefix[y]-prefix[x-1])