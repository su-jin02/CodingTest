# 강의섹션7. 미로의 최단거리 통로
import sys
from collections import deque
input = sys.stdin.readline
ch= [list(map(int, input().split())) for _ in range(7)]
visited = [[0] * 7 for _ in range(7)]

q = deque()
q.append([0,0, 0])
visited[0][0] = 1
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def canMove(x, y):
    if x < 0 or x > 6:
        return False
    if y < 0 or y > 6:
        return False
    return True

while q:
    x,y, dist = q.popleft()
    if x == 6 and y == 6:
        print(dist)
        break
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if canMove(tx,ty) and visited[tx][ty] == 0 and ch[tx][ty]==0:
            q.append([tx,ty, dist + 1])
            visited[tx][ty] = 1

else:
    print(-1)
