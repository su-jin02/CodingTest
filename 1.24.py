# 강의섹션7. 섬나라 아일랜드
import sys
from collections import deque
input = sys.stdin.readline
a = int(input())
island = [list(map(int, input().split())) for _ in range(a)]
res = 0
q = deque()

dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]

def canMove(x, y):
    if x < 0 or x > a-1:
        return False
    if y < 0 or y > a-1:
        return False
    return True

def BFS():
    while q:
        x,y = q.popleft()
        for i in range(8):
            tx = x+dx[i]
            ty = y+dy[i]
            if canMove(tx,ty) and island[tx][ty] == 1:
                island[tx][ty] = 0
                q.append([tx,ty])

for i in range(a):
    for j in range(a):
        if(island[i][j] == 1):
            q.append([i,j])
            island[i][j] = 0
            BFS()
            res += 1

print(res)