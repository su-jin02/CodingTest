#백준 python3로 실행시 시간초과가 발생하고 pypy3로 실행시 성공함
import sys
input = sys.stdin.readline
n = int(input())
res = 0
chess = [0] * n

def queen(col):
    global res
    for row in range(n):
        for i in range(col):
            if chess[i] == row or col-i == abs(chess[i] - row):
                break
        else:
            chess[col] = row
            if col == n-1:
                res += 1
                return
            else:
                queen(col+1)
queen(0)
print(res)