# https://www.acmicpc.net/problem/15663
import sys
input = sys.stdin.readline
def back(temp):
    if len(temp) == m:
        ans.add(tuple(temp))
        return
    for i in range(len(arr)):
        if visited[i] == 0:
            temp.append(arr[i])
            visited[i] = 1
            back(temp)
            temp.pop()
            visited[i] = 0
        
n,m = map(int,input().split())
arr = list(map(int,input().split()))
visited = [0] * n
ans,temp = set(),[]

back(temp)
for i in sorted(ans):
    print(*i)