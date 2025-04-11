def cubeditor(s):
    n = len(s)

    # 1. 접미사 배열 생성
    suffixes = sorted((s[i:], i) for i in range(n))
    print(suffixes,'suffixes')
    suffix_indices = [suffix[1] for suffix in suffixes]

    # 2. LCP 배열 계산
    lcp = [0] * n
    prev_suffix = suffixes[0][0]  # 첫 번째 접미사
    for i in range(1, n):
        current_suffix = suffixes[i][0]
        # 두 접미사의 공통 접두사 길이 계산
        common_length = 0
        while common_length < len(prev_suffix) and common_length < len(current_suffix) and \
              prev_suffix[common_length] == current_suffix[common_length]:
            common_length += 1
        lcp[i] = common_length
        prev_suffix = current_suffix
        print(lcp,'lcp')
    # 3. LCP 배열에서 최대값 찾기
    return max(lcp)

# 입력 받기
s = input().strip()
print(cubeditor(s))
