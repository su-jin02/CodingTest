import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline
n,m, st = map(int,input().split())
board = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)
visited = [0] * (n+1)
cnt = 1

def dfs(st):
    global cnt
    visited[st] = cnt
    board[st].sort()
    for i in board[st]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(st)
for i in range(1,n+1):
    print(visited[i])