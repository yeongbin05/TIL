def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


def kruskal(v,edges):
    
    edges.sort(key = lambda x:x[2])
    mst = []
    total_weight = 0
    for i,j,k in edges:
        if find(parent[i]) != find(parent[j]) :
            union(i,j)
            mst.append((i,j,k))
            total_weight += k

    return mst, total_weight
v, e = map(int, input().split())  # 정점 수와 간선 수
edges = [tuple(map(int, input().split())) for _ in range(e)]  # 간선 정보 (u, v, weight)
parent = [i for i in range(v+1)]
rank = [0] * (v + 1)
mst, total_weight = kruskal(v, edges)
print(total_weight)