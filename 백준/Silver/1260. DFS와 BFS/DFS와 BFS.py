#1260
import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, sys.stdin.readline().split())
q = deque()
graph = [[0]*(n+1) for _ in range(n+1)]

def DFS(x):
    for i in range(1, n + 1):
        if graph[x][i] == 1 and ch[i] == 0:
            print(i, end=' ')
            ch[i] = 1
            DFS(i)

def BFS(v):
    ch = [0] * (n + 1)
    q.append(v)
    ch[v] = 1
    while q:
        x = q.popleft()
        for i in range(1,n+1):
            if graph[x][i] == 1 and ch[i] == 0:
                q.append(i)
                ch[i] = 1
        print(x, end=' ')


for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

ch = [0] * (n + 1)
ch[v] = 1
print(v, end=' ')
DFS(v)
print()
BFS(v)
