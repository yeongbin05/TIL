def mod(a,b,c):
    ans = 1
    if b % 2 == 1:
        ans *= a
    else :
        
a,b,c = map(int,input().split())

print(mod(a,b,c))