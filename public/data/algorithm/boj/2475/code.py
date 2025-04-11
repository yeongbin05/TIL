nums = list(map(int,input().split()))
ans = 0
for i in nums:
    ans += i**2

print(ans%10)