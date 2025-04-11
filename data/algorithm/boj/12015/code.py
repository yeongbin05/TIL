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
