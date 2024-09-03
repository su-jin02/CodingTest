import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
res = ''

def quad(n, x, y):
    global res
    num = board[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if num != board[i][j]:
                res += '('
                quad(n // 2, x, y)
                quad(n // 2, x, y + n // 2)
                quad(n // 2, x + n // 2, y)
                quad(n // 2, x + n // 2, y + n // 2)
                res += ')'
                return
    res += str(num)

quad(n, 0, 0)
print(res)
