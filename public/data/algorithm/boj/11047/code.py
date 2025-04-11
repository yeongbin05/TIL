n,k = map(int,input().split())
value = sorted([int(input()) for _ in range(n)],reverse=True)
cnt = 0
for i in value:
    if i <= k :
        cnt += k//i
        k = k%i
        if k <= 0:
            break
print(cnt)