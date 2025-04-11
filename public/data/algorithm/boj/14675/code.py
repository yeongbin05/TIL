import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    # 단절점인지 -> 노드가 최상단인지 최하단인지만 체크
    if x == 1:
        if len(tree[y])  > 1 :
            print('yes')
        else:
            print('no')


    else:
        print('yes')