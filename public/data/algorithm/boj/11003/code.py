from collections import deque
import sys
input = sys.stdin.readline

def find_minimums(n, l, a):
    dq = deque()  # 덱 생성
    result = []   # 결과 저장

    for i in range(n):
        # 1. 윈도우 밖의 인덱스 제거
        if dq and dq[0] < i - l + 1:
            dq.popleft()
        
        # 2. 현재 값보다 큰 덱의 원소 제거
        while dq and a[dq[-1]] > a[i]:
            dq.pop()
        
        # 3. 현재 인덱스 추가
        dq.append(i)
        
        # 4. 결과에 최소값 추가
        result.append(a[dq[0]])
    
    return result

# 입력 처리

n, l = map(int,input().split())
a = list(map(int,input().split()))

# 결과 계산 및 출력
output = find_minimums(n, l, a)
print(' '.join(map(str, output)))
