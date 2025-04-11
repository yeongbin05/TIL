import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

heap=[]
max_h=0 #항상 주어지는 수는 양수

for i in range(N):
    heappush(heap, A[i])
    max_h = max(max_h, A[i])

v = heap[0]
curmax = max_h
min_diff = max_h - v

while heap[0] <= max_h: #최대 나올수 있는 min이 max_h까지 라는 거지, 그전에 min_diff가 나올 확률 큼
    v = heappop(heap) #heap[0] 의미
    min_diff = min(min_diff, curmax - v)
    heappush(heap, 2*v) #이때 넣은 2*v가 max보다 커질경우 2*v를 max로 인정(새로운 max가 등장할경우)
    curmax = max(curmax, 2*v)

print(min(min_diff, curmax-heap[0]))