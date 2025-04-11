def back(start):
    
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return 0
    for i in nums:
        if i not in arr:
            arr.append(i)
            back(i)
            arr.pop()


n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
arr = []
back(1)