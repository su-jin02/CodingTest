import sys
from collections import deque
input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(12)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 아래로 내리는 함수
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if board[j][i] != "." and board[k][i] == ".":
                    board[k][i] = board[j][i]
                    board[j][i] = "."
                    break


# 4칸인지 확인하는 함수 (BFS)
def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == board[x][y] and visited[nx][ny] == 0:
                q.append((nx, ny))
                temp.append((nx, ny))
                visited[nx][ny] = 1


# 4칸 이상일 때 삭제 함수
def delete(temp):
    for a, b in temp:
        board[a][b] = "."


ans = 0
while 1:
    flag = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                temp = []
                bfs(i, j)
                # 4칸 체크
                if len(temp) >= 4:
                    flag = 1
                    delete(temp)
    if flag == 0:
        break
    down()
    ans += 1

print(ans)