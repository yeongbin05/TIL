# input에서 strip안 써서 틀림
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = {}
cnt = 1
for _ in range(n):
    a = input().strip()
    dic[a] = cnt
    dic[cnt] = a
    cnt += 1
for i in range(m):
    b = input().strip()
    if b.isnumeric():
        print(dic[int(b)])
    else:
        print(dic[b])
