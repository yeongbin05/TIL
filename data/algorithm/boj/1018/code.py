n,m = map(int,input().split())
board = [input() for _ in range(n)]
ans = 3000

for i in range(n-8+1):
    for j in range(m-8+1):
        tempB = 0
        tempW = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                # 처음이 B로 기준
                if (a+b)% 2 == (i+j)%2:
                    if board[a][b]!= "B":
                        tempB += 1
                    else :
                        tempW += 1
                else :
                    if board[a][b] != 'W':
                        tempB += 1
                    else:
                        tempW += 1
        temp = min(tempB,tempW)
        if temp < ans:
            ans = temp

print(ans)