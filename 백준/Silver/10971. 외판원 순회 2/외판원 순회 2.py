import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n

def dfs(start, now, cnt, total):
    global res
    if cnt == n:
        if board[now][start] !=0:
            res = min(res, total+board[now][start])
        return
    if total > res:
        return

    for k in range(n):
        if board[now][k] !=0 and visited[k] == 0:
            visited[now] = 1
            dfs(start, k, cnt+1, total+board[now][k])
            visited[now] = 0


res = 1e9
for i in range(n):
    visited[i] = 1
    dfs(i, i, 1, 0)
    visited[i] = 0

print(res)