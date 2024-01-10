#백준1647 크루스칼알고리즘, union find
import sys
input = sys.stdin.readline

a,b = map(int, input().split())
ch = list(list(map(int, input().split())) for _ in range(b))
ch.sort(key=lambda x: x[2])
parent = [0] * (a+1)
for i in range(1,a+1):
    parent[i] = i

result = 0

def find(x):    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):  # 두 원소가 속한 집합을 합치기
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
last_edge = 0
for i,j,k in ch:
    if find(i) != find(j):
        union(i, j)
        answer += k
        last_edge = k
print(answer - last_edge)
