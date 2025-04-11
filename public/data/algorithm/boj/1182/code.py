from sys import stdin
input = stdin.readline
N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
def back(index):
    global cnt
    if sum(temp) == S :
        cnt += 1
        return
    
    for i in range(index,N):
        temp.append(num[i])
        back(i+1)
        temp.pop()



temp = []
back(0)
print(cnt)