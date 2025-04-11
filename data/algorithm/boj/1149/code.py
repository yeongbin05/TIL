import sys
input = sys.stdin.readline
n = int(input())
prices = [list(map(int,input().split()))  for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
dp[0] = prices[0]
for i in range(1,n):
    for j in range(3):
     
        dp[i][j] = min([value for k, value in enumerate(dp[i-1]) if k != j]) + prices[i][j]



print(min(dp[n-1]))