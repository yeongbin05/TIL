import sys 
input = sys.stdin.readline
n = int(input())
stack = []
nums = [int(input()) for _ in range(n)]
cnt = 0
ans = []
for i in range(1,n+1):
    stack.append(i)
    ans.append('+')
    while stack and stack[-1] == nums[cnt]:
        stack.pop() 
        cnt += 1
        ans.append('-')

if stack:
    print('NO')
else:
    for i in ans:
        print(i)