from collections import deque
n,k = map(int,input().split())
nums = deque(i for i in range(1,n+1))
index = 0
ans = []
while nums:
    for i in range(1,k+1):
        nums.append(nums.popleft())
    ans.append(nums.pop())

print('<',end='')
for i in range(len(ans)):
    print(ans[i],end="")
    if i != n-1:
       print(",",end= " ")
print('>')
