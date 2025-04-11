import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    flag = True
    n = int(input())
    nums = list(map(int,input().split()))
    in_degree = [0] * (n+1)
    nodes = [[] for _ in range(n+1)]
    for k in range(n-1):
        nodes[nums[k]] = nums[k+1:]
        in_degree[nums[k]] += len(nums[k+1:])
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        if a in nodes[b]:
            nodes[b].remove(a)
            in_degree[b] -= 1
            nodes[a].append(b)
            in_degree[a] += 1

        else:
            flag = False
            
            

    if flag == False:
        print('IMPOSSIBLE')
    else:
        sorted_indices = sorted(range(len(in_degree[1:])), key=lambda i: in_degree[1:][i], reverse=True)
        adjusted_indices = [i + 1 for i in sorted_indices]

        print(*adjusted_indices)