#백준1717 union find
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
x,y = map(int, input().split())
parent = [0] * (x+1)
for i in range(1,x+1):
    parent[i] = i

def find(x):    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):  # 두 원소가 속한 집합을 합치기
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        parent[b] = a

for _ in range(y):
    i, j, k = map(int, input().split())
    if i == 0:
        union(j,k)
    else:
        if(find(j) == find(k)):
            print("YES")
        else:
            print("NO")
