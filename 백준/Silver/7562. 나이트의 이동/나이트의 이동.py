import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
d = [
    [-2,1],
    [-2,-1],
    [-1,2],
    [-1,-2],
    [1,2],
    [1,-2],
    [2,1],
    [2,-1]]

for _ in range(n):
    chess = int(input())
    board = [[0]*chess for _ in range(chess)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    q = deque([(x1,y1)])
    while q:
        x,y = q.popleft()

        if x == x2 and y == y2:
            print(board[x][y])
            break

        for i in range(8):
            tx = x + d[i][0]
            ty = y + d[i][1]
            if 0<=tx<chess and 0<=ty<chess:
                if board[tx][ty] == 0:
                    board[tx][ty] = board[x][y] +1
                    q.append([tx,ty])