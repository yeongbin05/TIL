import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
max_dp = [[0] * n  for _ in range(n)]
min_dp = [[0] * n  for _ in range(n)]
max_dp[0],min_dp[0] = board[0],board[0]

for i in range(1,n):
    for j in range(n):2 
        if j == 0:
            max_dp[i][j] = max(max_dp[i-1][j],max_dp[i-1][j+1])+board[i][j]

        elif j == n - 1:
            max_dp[i][j] = max(max_dp[i-1][j-1],max_dp[i-1][j])+board[i][j]

        else:
            max_dp[i][j] = max(max_dp[i-1][j-1],max_dp[i-1][j],max_dp[i-1][j+1])+board[i][j]
for i in range(1,n):
    for j in range(n):
        if j == 0:
            min_dp[i][j] = min(min_dp[i-1][j],min_dp[i-1][j+1])+board[i][j]

        elif j == n - 1:
            min_dp[i][j] = min(min_dp[i-1][j-1],min_dp[i-1][j])+board[i][j]

        else:
            min_dp[i][j] = min(min_dp[i-1][j-1],min_dp[i-1][j],min_dp[i-1][j+1])+board[i][j]

print(max(max_dp[-1]),min(min_dp[-1]))
