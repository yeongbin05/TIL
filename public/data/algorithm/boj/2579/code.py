n = int(input())

dp = [0] * (n+1)
scores = [0] * (n+1)
for i in range(1,n+1):
    scores[i] = int(input())
if n == 1:
    print(scores[1])
elif n == 2:
    print(scores[1]+scores[2])
else:
    dp[1] = scores[1]
    dp[2] = scores[1]+scores[2]
    dp[3] = max(scores[1]+scores[3],scores[2]+scores[3])
    for i in range(4,n+1):
        dp[i] = max(dp[i-2]+scores[i],dp[i-3]+scores[i-1]+scores[i])
    # print(dp)
    print(dp[n])