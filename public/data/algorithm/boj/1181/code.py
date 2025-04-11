n = int(input())
word = list(set(input() for _ in range(n)))
word.sort(key = lambda x:(len(x),x))
for i in word:
    print(i)