import sys
input = sys.stdin.readline
n,q = map(int,input().split())
tempo = list(map(int,input().split()))
prefix = [0]*(n+1)

for i in range(1,n):
    prefix[i] = tempo[i] - tempo[i-1]
    if prefix[i] < 0 :
        prefix[i] = -prefix[i]

for _ in range(q):
    x,y = map(int,input().split())
    print(sum(prefix[x:y]))