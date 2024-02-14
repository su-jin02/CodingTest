#백준 10026 - BFS 적록색약
import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
a = int(input())
board = [list(map(str, input().strip())) for _ in range(a)]
visited1 = [[0] * a for _ in range(a)]
visited2 = [[0] * a for _ in range(a)]
res = 0
q1 = deque()
q2 = deque()
dx=[-1, 0, 0, 1]
dy=[0, 1, -1, 0]

def canMove(x, y):
    if x < 0 or x > a-1:
        return False
    if y < 0 or y > a-1:
        return False
    return True

def rgb(target): #적록색약 X
    while q1:
        x, y = q1.popleft()
        for k in range(4):
            tx = x + dx[k]
            ty = y + dy[k]
            if canMove(tx, ty) and board[tx][ty] == target and visited1[tx][ty] == 0:
                visited1[tx][ty] = 1
                q1.append([tx, ty])

def r_gb(): #적록색약 O
    while q2:
        x, y = q2.popleft()
        for k in range(4):
            tx = x + dx[k]
            ty = y + dy[k]
            if canMove(tx, ty) and visited2[tx][ty] == 0:
                if board[tx][ty] == 'R' or board[tx][ty] == 'G':
                    visited2[tx][ty] = 1
                    q2.append([tx, ty])

cnt1 = 0
cnt2 = 0
for i in range(a):
    for j in range(a):
        if visited1[i][j] == 0: #빠르게 계산하기 위해 위로 뺌
            if board[i][j] == 'R' or board[i][j] == 'G':
                q1.append([i,j])
                visited1[i][j] = 1
                cnt1 += 1
                rgb(board[i][j])
                if visited2[i][j] == 0:
                    q2.append([i,j])
                    visited2[i][j] = 1
                    cnt2 += 1
                    r_gb()

            else:
                q1.append([i, j])
                visited1[i][j] = 1
                cnt1 += 1
                cnt2 += 1
                rgb(board[i][j])

print(cnt1,cnt2)