import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]

res = 0
alpha = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global res
    res = max(res, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not board[nx][ny] in alpha:
            alpha.add(board[nx][ny])
            dfs(nx, ny, count+1)
            alpha.remove(board[nx][ny])

alpha.add(board[0][0])
dfs(0, 0, 1)
print(res)