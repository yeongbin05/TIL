import heapq
import sys

input = sys.stdin.readline


n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

# 시작 시간을 기준으로 정렬
lectures.sort(key=lambda x: (x[0], x[1]))

# 우선순위 큐 (강의실 별 종료 시간)
heap = []
heapq.heappush(heap, lectures[0][1])  # 첫 강의의 종료 시간을 추가

# 강의 배치
for i in range(1, n):
    start, end = lectures[i]
    # 가장 빨리 끝나는 강의실이 현재 강의 시작 시간보다 작거나 같으면 재사용
    if heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)  # 현재 강의의 종료 시간을 추가

# 최소 강의실 개수는 힙에 남아 있는 종료 시간의 개수
print(len(heap))
