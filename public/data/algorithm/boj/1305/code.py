def compute_pi(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

def find_shortest_ad_length(L, text):
    pi = compute_pi(text)
    # 주기의 길이 = 전체 길이 - 마지막 pi 값
    return L - pi[-1]

# 입력 처리
L = int(input())
text = input().strip()

# 결과 출력
print(find_shortest_ad_length(L, text))
