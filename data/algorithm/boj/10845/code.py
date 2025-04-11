import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    x = input().split()
    if len(x) == 1:
        x = x[0]
    else:
        x,y = x[0],x[1]

    if x == 'push':
        q.append(y)
    elif x== "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif x== 'size':
        print(len(q))
    elif x == 'empty':
        if q :
            print(0)
        else:
            print(1)

    elif x == 'front' :
        if not q :
            print(-1)
        else:
            print(q[0])
    elif x == 'back' :
        if not q :
            print(-1)
        else:
            print(q[-1])