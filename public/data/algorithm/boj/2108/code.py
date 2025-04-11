import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
print(round(sum(nums)/n))
print(sorted(nums)[n//2])
dic = {}
for i in nums:
    if i in dic:
        dic[i] += 1

    else:
        dic[i] = 1

Max = max([dic[i] for i in dic])
Max = [key for key,value in dic.items() if value == Max]
if len(Max) > 1:
    print(sorted(Max)[1])
else :
    print(Max[0])
print(max(nums)-min(nums))