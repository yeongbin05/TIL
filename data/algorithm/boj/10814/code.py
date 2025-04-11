import sys
input = sys.stdin.readline
n = int(input())
info = [input().split() for _ in range(n)]
# x[0]을 int로 해야지 string그대로 정렬하면 100이 20보다 앞이다
info.sort(key = lambda x : int(x[0]))
for i in info:
    print(i[0],i[1])