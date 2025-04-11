import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def back(N):
    if N == k :
        ans.add("".join(temp))
    for i in range(k):
        if check[i]:
            continue
        check[i] = 1
        temp.append(n[i])
        back(N+1)
        check[i] = 0
        temp.pop()


n = list(input().strip())
if '0' not in n:
    print(-1)
else:
    k = len(n)
    ans = set()
    check = [0] * k
    temp = []
    back(0)
    answer = 0
    for i in list(map(int,ans)):
        if i%30 == 0 and i > answer:
            answer = i
    if answer == 0:
        print(-1)
    else:
        print(answer)