import sys
from collections import deque
input = sys.stdin.readline
m,n,k = map(int, input().split())
squ = [list(map(int, input().split())) for _ in range(k)]
board = [[0] * n for _ in range(m)]

for x1,y1,x2,y2 in squ:
    for x in range(x1,x2):
        for y in range(y1,y2):
            board[y][x] = 1

q = deque()
res_list = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(res):
    while q:
        x, y = q.popleft()
        res += 1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0<=tx<m and 0<=ty<n and board[tx][ty] == 0:
                board[tx][ty] = 1
                q.append([tx,ty])
    return res

for y in range(n):
    for x in range(m):
        if board[x][y] == 0:
            q.append([x,y])
            board[x][y] = 1
            res_list.append(bfs(0))

print(len(res_list))
res_list.sort()
for i in res_list:
    print(i, end= ' ')
