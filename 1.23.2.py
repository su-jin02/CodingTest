# 강의섹션7. 미로탐색(DFS)
import sys
input = sys.stdin.readline
ch= [list(map(int, input().split())) for _ in range(7)]
visited = [[0] * 7 for _ in range(7)]

visited[0][0] = 1
dx=[-1,1,0,0]
dy=[0,0,1,-1]
res = 0

def canMove(x, y):
    if x < 0 or x > 6:
        return False
    if y < 0 or y > 6:
        return False
    return True

def DFS(x,y):
    global res
    if x == 6 and y == 6:
        res += 1
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if canMove(tx,ty) and visited[tx][ty] == 0 and ch[tx][ty] == 0:
                visited[tx][ty] = 1
                DFS(tx,ty)
                visited[tx][ty] = 0


DFS(0,0)
print(res)

