import sys
input = sys.stdin.readline
s1 = '0' + input().strip()
s2 = '0' + input().strip()
len_s1,len_s2 = len(s1),len(s2)
dp = [[0] * (len_s1) for _ in range(len_s2)]
string = [['' for _ in range(len_s1)] for _ in range(len_s2)]

for i in range(1,len_s2):
    for j in range(1,len_s1):
        if s2[i] == s1[j] :
            dp[i][j] = dp[i-1][j-1] + 1
            string[i][j] = string[i-1][j-1] + s2[i]
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            if len(string[i-1][j]) > len(string[i][j-1]):
                string[i][j] = string[i-1][j]
            else:
                string[i][j] = string[i][j-1]

# for i in dp:
#     print(i)
# for i in string:
#     print(i)
if dp[len_s2-1][len_s1-1] == 0:
    print(0)
else:
    print(dp[len_s2-1][len_s1-1])
    print(string[len_s2-1][len_s1-1])