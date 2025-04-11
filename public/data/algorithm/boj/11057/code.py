# https://www.acmicpc.net/problem/11057


n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [1] * 10

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = sum(dp[i-1][:j+1]) % 10007

print(sum(dp[-1]) % 10007)

# for i in dp:
#     print(i)