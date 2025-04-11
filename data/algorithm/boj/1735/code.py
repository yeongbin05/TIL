# 유클리드 호제
a,b = map(int,input().split())
c,d = map(int,input().split())

def gcd(x,y):
    while y > 0:
        x,y = y, x % y
    return x

x = c*b + a*d
y = b*d

print(int(x/gcd(x,y)),int(y/gcd(x,y)))

