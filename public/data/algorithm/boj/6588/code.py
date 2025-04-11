num = [i for i in range(2, 1000001)]
prime = []
for i in range(2, 1000001):
    if num[i - 2] != 0:
        for j in range(i, 1000001, num[i - 2]):
            num[j - 2] = 0

        prime.append(i)
print(prime[:10])
while 1:
    n = int(input())
    if n == 0:
        break
    break
