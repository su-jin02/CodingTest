from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global result
    q = deque()
    test_lab = deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if test_lab[i][j] == 2:
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if (0<=tx<n) and (0<=ty<m):
                if test_lab[tx][ty] == 0:
                    test_lab[tx][ty] = 2
                    q.append((tx,ty))



    #결과
    count = 0
    for i in range(n):

        for j in range(m):
            if test_lab[i][j] == 0:
                count += 1
    result = max(result, count)


def make_wall(count):
    if count == 3:
        
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(count+1)
                lab[i][j] = 0


n, m = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(n)]
result = 0
make_wall(0)
print(result)