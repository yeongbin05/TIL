n = int(input())
dp = [0] * (n+1)
dp[1] =  0
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 :
        dp[i] = min(dp[i//2]+1,dp[i]) 
    if i % 3 == 0 :
        dp[i] = min(dp[i//3]+1,dp[i]) 

print(dp[n])
# 빠른 풀이  
# import sys
# input = sys.stdin.readline
# memo = {}
# def f(x):
#     if x in memo:
#         return memo[x]
#     if x <= 1:
#         return 0
#     d1 = f(x // 3) + x % 3 + 1
#     d2 = f(x // 2) + x % 2 + 1
#     result =  min(d1, d2)
#     memo[x] = result
#     return result
# N = int(input())
# print(f(N))