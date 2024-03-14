import sys
input = sys.stdin.readline
board = [list(map(str, input().strip())) for _ in range(5)]
for i in range(15):
    for j in range(5):
        #처음 코드
        # try:
        #     print(board[j][i], end='')
        # except:
        #     continue
        if i < len(board[j]):
            print(board[j][i], end="")