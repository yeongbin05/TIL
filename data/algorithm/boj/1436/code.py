n = int(input())
cnt = 1
temp = 666
if n == 1:
    print(666)
else:
    while cnt < n :
        temp += 1
        if '666' in str(temp):
            cnt += 1
            
    print(temp)
