s1 = input()
s2 = input()
s3 = input()
len_s1,len_s2,len_s3 = len(s1),len(s2),len(s3)
dp = [[[0] * (len_s1+1) for _ in range(len_s2+1)] for i in range(len_s3+1)]

for i in range(1,len_s3+1):
    for j in range(1,len_s2+1):
        for k in range(1,len_s1+1):
            if s3[i-1] == s2[j-1] == s1[k-1] :
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

print(dp[len_s3][len_s2][len_s1])