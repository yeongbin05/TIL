n,m = map(int,input().split())
nums = list(map(int,input().split()))
start = 0
end = 1
temp = 0 
ans = 0
temp = nums[start] + nums[end]
while 1:
    
    
    if temp == m :
        ans += 1
        end += 1
        start += 1
        if end >= n or start>=n:
            break
        temp = nums[start]+ nums[end]
    elif temp < m :
        end += 1
        if end >= n:
            break
        temp += nums[end]
    else :
        temp -= nums[start]
        start += 1
    if start > n  or end > n :
        break
   
print(ans)
