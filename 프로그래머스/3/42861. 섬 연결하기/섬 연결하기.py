def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    parent = [i for i in range(n)]
        
    # 비용 순으로 정렬
    costs.sort(key=lambda x: x[2])
        
    answer = 0
    for a, b, cost in costs:
        # 사이클이 발생하지 않으면 연결
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    
    return answer