# 강의섹션7. 등산경로
import sys
input = sys.stdin.readline
a = int(input())
ch= [list(map(int, input().split())) for _ in range(a)]
visited = [[0] * a for _ in range(a)]
start = [0,0,10000]
end = [0,0,0]

for i in range(a):
    for j in range(a):
        if ch[i][j] < start[2]:
            start[0] = i
            start[1] = j
            start[2] = ch[i][j]
        if ch[i][j] > end[2]:
            end[0] = i
            end[1] = j
            end[2] = ch[i][j]
res = 0
dx=[-1, 0, 0, 1]
dy=[0, 1, -1, 0]

def DFS(x,y,value):
    global res
    if x == end[0] and y == end[1]:
        res += 1
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if(0 <= tx < a and 0 <= ty < a and visited[tx][ty] == 0):
                if ch[tx][ty] > value:
                    visited[tx][ty] = 1
                    DFS(tx,ty, ch[tx][ty])
                    visited[tx][ty] = 0

visited[start[0]][start[1]] = 1
DFS(start[0], start[1], start[2])
print(res)
