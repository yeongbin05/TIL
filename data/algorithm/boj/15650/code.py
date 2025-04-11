def back(start):
    
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    for i in range(start,n+1):
        if i not in arr:
            arr.append(i)
            back(i+1)
            arr.pop()


n,m = map(int,input().split())
arr = []
back(1)