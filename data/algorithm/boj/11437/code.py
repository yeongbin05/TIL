def dfs(node, parent_node):
    parent[node] = parent_node  # 부모 설정
    depth[node] = depth[parent_node] + 1  # 깊이 설정
    for child in tree.get(node, []):  # 자식 노드 탐색
        if child != parent_node:  # 부모로 되돌아가는 경우 방지
            dfs(child, node)


def lca(x, y):
    # 깊이를 동일하게 맞추기
    while depth[x] > depth[y]:
        x = parent[x]
    while depth[y] > depth[x]:
        y = parent[y]

    # 공통 조상을 찾을 때까지 위로 이동
    while x != y:
        x = parent[x]
        y = parent[y]

    return x


# 입력 받기
n = int(input())
tree = {}

for _ in range(n - 1):  # 트리는 n-1개의 간선
    u, v = map(int, input().split())
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    tree[u].append(v)
    tree[v].append(u)

# 루트 노드 설정
root = 1

# 부모와 깊이 테이블 초기화
parent = [0] * (n + 1)
depth = [0] * (n + 1)

# DFS를 통해 부모와 깊이를 계산
dfs(root, 0)
print(depth)
print(parent)
# 최소 공통 조상 쿼리 처리
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))
