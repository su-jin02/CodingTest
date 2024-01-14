#백준1976 union find
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
x = int(input())
y = int(input())
parent = [i for i in range(x+1)]

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

for i in range(x):
    ch = list(map(int, input().split()))
    for j in range(x):
        if(i == j):
            break
        else:
            if(ch[j] == 1):
                union(j+1, i+1)

result = list(map(int, input().split()))
for i in range(1,y):
    if(find(result[i]) != find(result[0])):
        print("NO")
        break
else:
    print("YES")