m,n = map(int,input().split())
prime = [0] * (n+1)
primes = []
for i in range(2,n+1):
    if prime[i] == 0:
        if m<=i<=n:
            primes.append(i)
        for j in range(i,n+1,i):
            prime[j] = 1

for i in primes:
    print(i)