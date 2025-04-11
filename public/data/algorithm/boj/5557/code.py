n = int(input())
nums = list(map(int, input().split()))

# DP 배열 초기화: dp[i][x]는 i번째 숫자까지 고려했을 때 결과가 x인 경우의 수
dp = [[0] * 21 for _ in range(n)]
dp[0][nums[0]] = 1  # 첫 번째 숫자 초기화

# DP 계산
for i in range(1, n - 1):
    for j in range(21):  # 가능한 중간 결과 (0 <= j <= 20)
        if dp[i - 1][j] > 0:  # 이전 결과가 유효한 경우만 계산
            if j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i - 1][j]
            if j - nums[i] >= 0:
                dp[i][j - nums[i]] += dp[i - 1][j]

# 최종 결과: 마지막 숫자와 동일한 결과를 만드는 경우의 수
print(dp[n - 2][nums[-1]])
