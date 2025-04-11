import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
m = int(input())

if sum(nums) < m:
    print(max(nums))

else :
    start, end = 0,max(nums)
    while start <= end :
        temp = 0
    
        mid = (start+end) // 2

        for i in nums : 
            if i < mid :
                temp += i
            else :
                temp += mid
        
        if temp >  m :
            end = mid - 1
        
       
        else:
            start = mid + 1
        # print(mid,'mid')
    print(end)