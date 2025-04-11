n = int(input())
cnt2 = 0
cnt5 = 0
for i in range(1,n+1):
    
    while i % 2 == 0 :
        i = i // 2
        cnt2 += 1
    while i % 5 == 0 :
        i = i // 5
        cnt5 += 1

print(min(cnt2,cnt5))