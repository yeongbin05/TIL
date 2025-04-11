import sys
input = sys.stdin.readline
s = input().strip()
boom = input().strip()
lenB = len(boom)
stack = []

for i in s:
    stack.append(i)
    if ''.join(stack[-lenB:]) == boom:
        for j in range(lenB):
            stack.pop()

if stack:
    print(*stack,sep="")
else:
    print('FRULA')