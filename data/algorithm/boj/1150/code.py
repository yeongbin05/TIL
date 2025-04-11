def min_cable_length(n, k, positions):
    # 거리 차이를 계산하여 저장
    distances = []
    for i in range(n - 1):
        distances.append(positions[i + 1] - positions[i])
    
    # 모든 거리 차이를 고려하는 배열 생성
    dp = [float('inf')] * (k + 1)
    dp[0] = 0  # 0개의 쌍 선택 시 길이는 0

    # 거리 차이를 기반으로 동적 프로그래밍
    for i in range(n - 1):
        for j in range(k, 0, -1):
            # 쌍을 선택할 경우
            if j - 1 >= 0:
                dp[j] = min(dp[j], dp[j - 1] + distances[i])

    return dp[k]

# 주어진 입력값
n = 5
k = 2
positions = [1, 3, 4, 6, 12]

# 결과 계산
result = min_cable_length(n, k, positions)
print(result)  # 결과 출력
