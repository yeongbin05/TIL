from collections import deque
def bfs(idx):
    arr[idx] = 0
    q = deque()
    q.append(idx)
    while q:
        if arr[m] != -1:
            break
        start = q.popleft()
        for a in (start+1,start-1,start*2):
            if 0<=a<100001 and arr[a] == -1:
                arr[a] = arr[start] + 1
                q.append(a)
            
n,m = map(int,input().split())
arr = [-1 for _ in range(100001)]
bfs(n)
print(arr[m])
