#백준2178 미로찾기(BFS)
#DFS는 시간초과 발생
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board= [list(map(int, input().strip())) for _ in range(n)]
dis= [[0] * m for _ in range(n)]

q = deque()
q.append([0,0])
dis[0][0] = 1
dx=[-1,1,0,0]
dy=[0,0,1,-1]

while q:
    x,y = q.popleft()
    global res, cnt
    if x == n-1 and y == m-1:
        print(dis[n-1][m-1])
        exit()
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0<= tx <n and 0<= ty <m and board[tx][ty] == 1 and dis[tx][ty] == 0:
                q.append([tx, ty])
                dis[tx][ty] = dis[x][y] + 1


