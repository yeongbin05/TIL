n = int(input())
m = int(input())
s = input()
p = 'I'

p += 'OI' * n
idx = 0
length = len(p)
ans = 0
while 1 :
    if s[idx:idx+length] == p :
        ans += 1
        idx += 2
        
    else : 
        idx += 1
    if idx > m - length :
        break

print(ans)