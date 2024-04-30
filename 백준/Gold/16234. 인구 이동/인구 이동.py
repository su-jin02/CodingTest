from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    union = []
    q.append((i, j))
    union.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))
    return union


result = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = 1
                    people = sum(board[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        board[x][y] = people

    if flag == 0:
        print(result)
        break

    result += 1
