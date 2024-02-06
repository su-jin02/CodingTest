# 백준7569 토마토(DFS)
import sys
from collections import deque
input = sys.stdin.readline
width, height, depth = map(int, input().split()) #가로, 세로, 높이
board= [[list(map(int, input().split())) for _ in range(height)] for _ in range(depth)]
dis = [[[0] * width for _ in range(height)] for _ in range(depth)]
q = deque()
dx=[-1, 0, 0, 1, 0, 0]
dy=[0, 1, -1, 0, 0, 0]
dz=[0, 0, 0, 0, 1, -1]

def canMove(z, x, y):
    if x < 0 or x > height-1:
        return False
    if y < 0 or y > width-1:
        return False
    if z < 0 or z > depth-1:
        return False
    return True

for k in range(depth):
    for i in range(height):
        for j in range(width):
            if (board[k][i][j] == 1):
                q.append([k, i, j])

while q:
    for i in range(len(q)):
        z,x,y = q.popleft()
        for i in range(6):
            tz = z+dz[i]
            tx = x+dx[i]
            ty = y+dy[i]
            if canMove(tz,tx,ty) and board[tz][tx][ty] == 0:
                    board[tz][tx][ty] = 1
                    dis[tz][tx][ty] = dis[z][x][y] + 1
                    q.append([tz,tx,ty])
flag=1
for k in range(depth):
    for i in range(height):
        for j in range(width):
            if board[k][i][j]==0:
                flag=0
result=0
if flag==1:
    for k in range(depth):
        for i in range(height):
            for j in range(width):
                if dis[k][i][j]>result:
                    result=dis[k][i][j]
    print(result)
else:
    print(-1)