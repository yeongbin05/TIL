def back(start):
    
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return 0
    for i in range(start,n+1):
        
            arr.append(i)
            back(i)
            arr.pop()


n,m = map(int,input().split())
arr = []
back(1)