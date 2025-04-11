n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    cnt = 1
    for j in range(n):
        if j != i and info[j][0]>info[i][0] and info[j][1]>info[i][1]:
            cnt += 1
    print(cnt, end= " ")
