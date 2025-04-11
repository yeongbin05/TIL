n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    big,small = max(x,y),min(x,y)
    num = 1
    denom = 1
    temp_small = small
    for i in range(small):
        num *= big
        big -= 1
        denom *= temp_small
        temp_small -= 1
    print(num//denom)