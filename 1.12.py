#백준4195 union find
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
        # return find(parent[x])
    return x

def union(a, b):  # 두 원소가 속한 집합을 합치기
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        parent[b] = a
        visited[a] += visited[b]

for _ in range(int(input())):
    parent = dict()
    visited = dict()
    for _ in range(int(input())):
        a,b = map(str, input().split())

        if a not in parent:
            parent[a] = a
            visited[a] = 1

        if b not in parent:
            parent[b] = b
            visited[b] = 1

        union(a,b)

        print(visited[find(a)])