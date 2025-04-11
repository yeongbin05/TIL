import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nums = list(map(int,input().split()))
start = 0
end = max(nums)

while start <= end :
    temp = 0
    mid = (start + end) // 2
    for i in nums:
        if i > mid :
            temp += i - mid

    if temp >= m :
        start = mid + 1

    elif temp < m :
        end = mid - 1
    # print(start,end,mid,temp)
print(end)
