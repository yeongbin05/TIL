s1 = '0' + input()
s2 = '0' + input()
len_s1,len_s2 = len(s1),len(s2)
dp = [[0] * (len_s1) for _ in range(len_s2)]

for i in range(1,len_s2):
    for j in range(1,len_s1):
        if s2[i] == s1[j] :
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[len_s2-1][len_s1-1])