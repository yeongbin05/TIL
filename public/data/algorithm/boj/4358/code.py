import sys
input = sys.stdin.readline
dic = {}
cnt = 0
while 1:
    
    a = input().strip()
    if a == '':
        break
    if a in dic:
        dic[a] += 1
        cnt += 1
    else:
        dic[a] = 1
        cnt += 1


for key in sorted(dic):
    
    # print(key,round(dic[key]/cnt*100,4))
    percentage = round(dic[key] / cnt * 100, 4)
    print(f"{key} {percentage:.4f}")