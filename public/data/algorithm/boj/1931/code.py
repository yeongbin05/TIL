import sys
input = sys.stdin.readline
n = int(input())
time_table = [list(map(int,input().split())) for _ in range(n)]
time_table.sort(key = lambda x : (x[1],x[0]))
end_time = time_table[0][1]
cnt = 1
print(time_table)
for i in range(1,n):
    if time_table[i][0] >= end_time :
        end_time = time_table[i][1]
        cnt += 1

print(cnt)