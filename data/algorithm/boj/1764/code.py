import sys
input = sys.stdin.readline
n,m= map(int,input().split())
dic = {}
ans = []
for i in range(n):
    a = input().strip()
    if a not in dic:
        dic[a] = 1
for i in range(m):
    b = input().strip()
    if b in dic:
        ans.append(b)
print(len(ans))

for i in sorted(ans):
    print(i)