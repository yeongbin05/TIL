w, h = map(int, input().split())
mod = 100000
dp = [[[[0] * 2 for _ in range(2)] for _ in range(101)] for _ in range(101)]
for i in range(2, w + 1) :
    dp[i][1][0][0] = 1
for i in range(2, h + 1) :
    dp[1][i][1][0] = 1
for i in range(2, w + 1) :
    for j in range(2, h + 1) :
        dp[i][j][0][0] = (dp[i - 1][j][0][0] + dp[i - 1][j][0][1]) % mod;
        dp[i][j][0][1] = dp[i - 1][j][1][0];
        dp[i][j][1][0] = (dp[i][j - 1][1][0] + dp[i][j - 1][1][1]) % mod;
        dp[i][j][1][1] = dp[i][j - 1][0][0];
ans = 0
for i in range(2) :
    for j in range(2) :
        ans += dp[w][h][i][j]
print(ans % mod)
