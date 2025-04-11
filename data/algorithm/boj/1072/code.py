import math

x, y = map(int, input().split())

# 첫 번째 승률 계산
first = math.floor(y / x * 100)

start = 0
end = x - y
result = -1  # 결과를 저장할 변수

# 이진 탐색
while start <= end:
    mid = (start + end) // 2
    second = math.floor((y + mid) / (x + mid) * 100)

    # 승률이 증가했다면, mid를 기록하고 탐색 범위를 줄임
    if second > first:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
