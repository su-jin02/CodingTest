import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board=[]
maxx = 0
for _ in range(n):
    a = list(map(int, input().split()))
    if max(a) > maxx:
        maxx = max(a)
    board.append(a)

q = deque()
dx=[-1, 0, 0, 1]
dy=[0, 1, -1, 0]
res = 0

def canMove(x, y):
    if x < 0 or x > n-1:
        return False
    if y < 0 or y > n-1:
        return False
    return True

for h in range(maxx):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if board[j][k] > h and visited[j][k] == 0:
                q.append([j,k])
                visited[j][k] = 1
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        tx = x + dx[i]
                        ty = y + dy[i]
                        if canMove(tx, ty) and board[tx][ty] > h and visited[tx][ty] == 0:
                            visited[tx][ty] = 1
                            q.append([tx, ty])
                cnt += 1
    if cnt > res:
        res = cnt

print(res)
