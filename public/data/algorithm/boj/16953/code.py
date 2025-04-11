from collections import deque
def bfs(num):
    q = deque([(num,1)])
    while q:
        now,cnt = q.popleft()
        if now > b :
            continue
        if now == b:
            print(cnt)
            break
        i,j = int(now*2),int(str(now) + '1')
        q.append((i,cnt+1))
        q.append((j,cnt+1))
    else:
        print(-1)
        
a,b = map(int,input().split())
bfs(a)