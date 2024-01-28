# 강의섹션7. 토마토
import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int, input().split()) #가로, 세로
ch= [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]
q = deque()
dx=[-1, 0, 0, 1]
dy=[0, 1, -1, 0]

def canMove(x, y):
    if x < 0 or x > n-1:
        return False
    if y < 0 or y > m-1:
        return False
    return True


for i in range(n):
    for j in range(m):
        if (ch[i][j] == 1):
            q.append([i, j])

while q:
    for i in range(len(q)):
        x,y = q.popleft()
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if canMove(tx,ty) and ch[tx][ty] == 0:
                ch[tx][ty] = 1
                dis[tx][ty] = dis[x][y] + 1
                q.append([tx,ty])

flag=1
for i in range(n):
    for j in range(m):
        if ch[i][j]==0:
            flag=0
result=0
if flag==1:
    for i in range(n):
        for j in range(m):
            if dis[i][j]>result:
                result=dis[i][j]
    print(result)
else:
    print(-1)