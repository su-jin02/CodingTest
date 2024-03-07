#1260
import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, sys.stdin.readline().split())
q = deque()
graph = [[] for _ in range(n+1)]
DFS_ch = [0] * (n + 1)
BFS_ch = [0] * (n + 1)

def DFS(x):
    print(x, end=' ')
    DFS_ch[x] = 1
    for i in graph[x]:
        if DFS_ch[i] == 0:
            DFS(i)

def BFS(v):
    q.append(v)
    BFS_ch[v] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if BFS_ch[i] == 0:
                q.append(i)
                BFS_ch[i] = 1
        print(x, end=' ')

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()
    
DFS(v)
print()
BFS(v)
