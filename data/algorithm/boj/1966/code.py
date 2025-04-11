from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    nums = deque([i,j] for i,j in enumerate(nums))
    cnt = 0
    while 1:
        if nums[0][1] == max([i[1] for i in nums]):
            cnt += 1
            if nums[0][0] == m:
                print(cnt)
                break
            nums.popleft()
            
        else:
            nums.append(nums.popleft())

        