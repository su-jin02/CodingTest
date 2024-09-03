from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[y][x] = True
    removed = list()

    while q:
        x, y = q.popleft()
        zero = 0
        for k in range(4):
            ax, ay = x + dx[k], y + dy[k]
            if -1 < ax < m and -1 < ay < n:
                if board[ay][ax] > 0 and not visited[ay][ax]:
                    visited[ay][ax] = True
                    q.append((ax, ay))
                elif board[ay][ax] == 0:
                    zero += 1

        if zero:
            removed.append((x, y, zero))

    return removed


def search():
    bfs_cnt = 0
    visited = [[False] * m for _ in range(n)]
    removed = list()

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and not visited[i][j]:
                removed.extend(bfs(j, i, visited))
                bfs_cnt += 1

    for x, y, zero in removed:
        board[y][x] = max(board[y][x] - zero, 0)

    return bfs_cnt


def solve():
    t = 1
    while True:
        bfs_cnt = search()
        if bfs_cnt >= 2:
            return t - 1
        if bfs_cnt == 0:
            return 0
        t += 1


print(solve())
