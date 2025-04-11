import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    if n == 1:
        print(max(arr[0][0],arr[1][0]))
        continue
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1],dp[1][1] = arr[0][0],arr[1][0]
    dp[0][2],dp[1][2] = arr[1][0]+arr[0][1],arr[0][0] + arr[1][1]
    for i in range(3,n+1):
        dp[0][i] = max(dp[1][i-1]+arr[0][i-1],dp[1][i-2]+arr[0][i-1])
        dp[1][i] = max(dp[0][i-2]+arr[1][i-1],dp[0][i-1]+arr[1][i-1])
        # print(dp,'dp')


    print(max(dp[0][-1],dp[1][-1]))