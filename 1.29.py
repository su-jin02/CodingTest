# 강의섹션7. 사다리타기(DFS) #도착지에서 출발하기
import sys
from collections import deque
input = sys.stdin.readline
ch= [list(map(int, input().split())) for _ in range(10)]
visited = [[0] * 10 for _ in range(10)]
q = deque()
dx=[0, 0, -1]
dy=[1, -1, 0]

def DFS(x,y):
    if x == 0:
        print(y)
        exit()
    else:
        for i in range(3):
            xx = x + dx[i]
            yy = y + dy[i]
            if(0 <= xx < 10 and 0 <= yy < 10 and ch[xx][yy] == 1 and visited[xx][yy]==0):
                visited[xx][yy] = 1
                DFS(xx,yy)
                break

for k in range(10):
    if(ch[9][k] == 2):
        visited[9][k] = 1
        DFS(9,k)
