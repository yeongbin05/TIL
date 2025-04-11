n = int(input())
dic = {}
a = input().split()
for i in a:
    if i not in dic:
        dic[i] = 1

m = int(input())
b = input().split()
for j in b:
    if j in dic:
        print(1)
    else:
        print(0)