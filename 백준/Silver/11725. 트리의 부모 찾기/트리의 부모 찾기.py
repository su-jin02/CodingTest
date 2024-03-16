import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n=int(input())
res = [0]*(n+1)
graph = {}
for j in range(1,n+1):
    graph[j] = []

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def search(i):
    for j in graph[i]:
        if res[j] == 0:
            res[j] = i
            search(j)

res[1] = 1
search(1)
for i in range(2,n+1):
    print(res[i])