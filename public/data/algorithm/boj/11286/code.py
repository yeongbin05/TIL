"""
https://www.acmicpc.net/problem/11286
"""
import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    
    x = int(input())
    if x != 0:
        # 절대값과 원래 값을 튜플로 저장
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            # 우선 순위가 가장 높은 원소 (절대값 기준, 같으면 원래 값 기준)
            print(heapq.heappop(heap)[1]) 