def can_divide(lectures, max_size, M):
    count = 1  # 블루레이 개수
    current_sum = 0

    for lecture in lectures:
        if current_sum + lecture > max_size:
            count += 1
            current_sum = lecture  # 새로운 블루레이 시작
        else:
            current_sum += lecture

    return count <= M

def find_minimum_bluray_size(N, M, lectures):
    left, right = max(lectures), sum(lectures)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_divide(lectures, mid, M):
            result = mid  # 조건을 만족하면 결과 저장
            right = mid - 1  # 더 작은 크기를 시도
        else:
            left = mid + 1  # 더 큰 크기를 시도

    return result

# 입력 처리
N, M = map(int, input().split())
lectures = list(map(int, input().split()))

# 최소 블루레이 크기 출력
print(find_minimum_bluray_size(N, M, lectures))
