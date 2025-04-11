# ans = 0
# temp = 0
# problems = [list(map(int,input().split())) for _ in range(11)]
# problems.sort(key = lambda x:x[0])
# for i in range(11):
#     x,y = problems[i][0],problems[i][1]
#     ans += (temp + y*20)
#     temp += x

# print(ans)
import sys

input = sys.stdin.readline

time = [list(map(int,input().split())) for _ in range(11)]
time.sort()
# print(time)
sum = 0
pen = 0
for v,d in time:
    sum += v
    pen += sum+20*d
print(pen)