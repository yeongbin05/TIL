# 입력 처리
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
dp = [0] * (K + 1)  # 배낭 무게 제한 K까지의 DP 테이블 초기화

for weight,value in items:
    for i in range(K,weight-1,-1):
        dp[i] = max(dp[i],dp[i-weight] + value)
print(dp[K])