import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    x = input().split()
    if len(x) == 2:
        x,y = x[0],x[1]
    else:
        x = x[0]
    if x == 'push':
        stack.append(y)
    elif x == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
        
    elif x == 'size':
        print(len(stack))
    
    elif x == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif x == 'top':
        if not stack:
            print(-1)
        else :
            print(stack[-1])