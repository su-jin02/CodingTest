import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sink = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'X': # 인접한 세칸 이상이 바다인지 확인
            count = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < r and 0 <= y < c:
                    if board[x][y] == '.':
                        count += 1
                else:
                    count += 1
            if count >= 3:
                sink.append((i, j))

if len(sink) > 0:
    for x, y in sink:
        board[x][y] = '.'

row = []
col = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            row.append(i)
            col.append(j)

if row:
    row1 = min(row)
    row2 = max(row)
    col1 = min(col)
    col2 = max(col)
    for i in range(row1, row2 + 1):
        for j in range(col1, col2 + 1):
            print(board[i][j], end="")
        print()
else:
    print('X')