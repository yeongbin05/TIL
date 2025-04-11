import sys
input = sys.stdin.readline
n,m  = map(int,input().split())
pipes = list(map(int,input().split()))
arr = [0] * (max(pipes)+1)

for i in pipes :
    arr[i] = 1

ans = 0

for i in range(len(arr)):
    if arr[i] != 0 :
        ans += 1
        for j in range(m):
            if i+j < len(arr):
                arr[i+j] = 0

print(ans)