import heapq

n = int(input())
hq = []
for _ in range(n):
    x = int(input())
    heapq.heappush(hq, x)
    print(hq)
