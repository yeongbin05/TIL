n = int(input())
cards = list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = cards[0]
