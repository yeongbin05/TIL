# from itertools import permutations
# n = int(input())
# k = int(input())
# cards = [input() for _ in range(n)]

# nCr = list(permutations(cards,k))
# dic = {}
# for i in nCr:
#     temp = ""
#     for j in i:
#         temp += j
#     if temp not in dic:
#         dic[temp] = 1
# print(len(dic))

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
ans = set()
temp = []
check = [0] * (n)
def back(N):
    if N == k:
        ans.add(''.join(temp))

    for i in range(n):
        if check[i]:
            continue
        check[i] = True

        temp.append(cards[i])
        back(N+1)
        check[i] = False
        temp.pop()

back(0)
print(ans)