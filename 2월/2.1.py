# 강의섹션8. 알리바바와 40인의 도둑(Top-Down)
import sys
input = sys.stdin.readline
a =int(input())
board = [list(map(int, input().split())) for _ in range(a)]
dp = [[0] * a for _ in range(a)]

def DFS(x,y):
    if dp[x][y] > 0:
        return dp[x][y]
    if x==0 and y==0:
        return board[0][0]
    else:
        if x == 0:
            dp[x][y] = DFS(x,y-1) + board[x][y]
        elif y == 0:
            dp[x][y] = DFS(x-1,y) + board[x][y]
        else:
            dp[x][y] = min(DFS(x,y-1),DFS(x-1,y)) + board[x][y]
        return dp[x][y]

print(DFS(a-1,a-1))