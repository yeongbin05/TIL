def compute_pi(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1,m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    pi = compute_pi(pattern)
    j = 0  # 패턴 포인터
    cnt = 0
    ans = []

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]  # 이전 일치 위치로 이동
        if text[i] == pattern[j]:
            if j == m - 1:  # 패턴이 완전히 일치
                cnt += 1
                ans.append(i - m + 2)  # 시작 위치 (1-based index)
                j = pi[j]  # 다음 검색을 위해 이동
            else:
                j += 1
    return cnt, ans

# 입력 받기
t = input()
p = input()

# KMP 수행
count, positions = kmp_search(t, p)

# 결과 출력
print(count)
print(*positions)
