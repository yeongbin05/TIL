import sys
input = sys.stdin.readline
n = int(input())
sanggeun = list(map(int,input().split()))
dic = {}
for i in sanggeun:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
m = int(input())
how_many = list(map(int,input().split()))
for i in how_many:
    if i in dic:
        print(dic[i],end=" ")
    else:
        print(0,end= " ")