t = int(input())
for _ in range(t):
    n = int(input())
    cards = [list(map(int, input().split())) for i in range(2)]
    if n == 1:
        print(max(cards[0][0], cards[1][0]))
        continue
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][0], dp[1][0] = cards[0][0], cards[1][0]
    dp[0][1], dp[1][1] = max(cards[1][0] + cards[0][1], cards[0][0]), max(
        cards[0][0] + cards[1][1], cards[1][0]
    )
    print(dp)
    for k in range(3, n):
        print(k)
        dp[k] = max(
            cards[0][k - 1] + dp[1][k - 2],
            cards[1][k - 1] + dp[0][k - 3],
            cards[1][k - 1] + dp[0][k - 2],
            cards[0][k - 1] + dp[1][k - 3],
        )
    print(dp)
