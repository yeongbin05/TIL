# import sys
# input = sys.stdin.readline
# n = int(input())
# nums = [input().split() for _ in range(n)]


# graph = [[] for _ in range(n)]
# graph[0] = [int(nums[0][0])]
# for i in range(n-1):
#     for j in range(i+1):
        
#         parent = int(graph[i][j])
#         graph[i+1].append(parent+int(nums[i+1][j]))
#         graph[i+1].append(parent+int(nums[i+1][j+1]))

# print(max(graph[-1]))

import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

# DP 배열을 한 줄씩 처리
dp = nums[0]  # 첫 번째 행은 그대로 dp로 사용

for i in range(1, n):
    new_dp = []
    for j in range(i + 1):
        if j == 0:
            new_dp.append(dp[0] + nums[i][0])  # 첫 번째 열
        elif j == i:
            new_dp.append(dp[i-1] + nums[i][i])  # 마지막 열
        else:
            new_dp.append(max(dp[j-1], dp[j]) + nums[i][j])  # 중간 열
    dp = new_dp  # dp를 갱신
print(dp)
print(max(dp))  # 마지막 행에서 최대값 출력
