import sys

input = sys.stdin.readline
s = input().strip()
q = int(input())
length = len(s)
dic = {}
prefix = [{} for _ in range(length)]
cnt = 1

for i in range(length):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1
    prefix[i] = dic.copy()

# print(prefix)

for i in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    if a in prefix[r]:
        right = prefix[r][a]
    else:
        right = 0
    if l == 0:
        left = 0
    else:
        if a in prefix[int(l) - 1]:
            left = prefix[int(l) - 1][a]
        else:
            left = 0
    print(right - left)
