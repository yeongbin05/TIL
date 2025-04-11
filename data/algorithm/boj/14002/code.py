import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):

    for j in range(i, n):
        if nums[j] > nums[i]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
cnt = max(dp)
ans = []
for i in range(n - 1, -1, -1):
    if dp[i] == cnt:
        ans.append(nums[i])
        cnt -= 1
print(*ans[::-1])
