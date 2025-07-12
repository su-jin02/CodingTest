from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    # 사각형 테두리는 1, 내부는 2
    for rec in rectangle:
        x1, y1, x2, y2 = [c * 2 for c in rec]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 2  # 내부
                elif board[i][j] != 2:
                    board[i][j] = 1  # 외곽선

    sx, sy = characterX * 2, characterY * 2
    ex, ey = itemX * 2, itemY * 2

    # bfs탐색
    tx = [0, 0, -1, 1]
    ty = [1, -1, 0, 0]
    visited = [[0] * 102 for _ in range(102)]
    q = deque([[sx, sy, 0]])

    while q:
        x, y, k = q.popleft()
        if x == ex and y == ey:
            return k//2
        for i in range(4):
            nx = x + tx[i]
            ny = y + ty[i]
            if 0 <= nx  <= 102 and 0 <= ny <= 102 and visited[nx][ny] == 0 and board[nx][ny] == 1:
                    q.append([nx, ny, k + 1])
                    visited[nx][ny] = 1
                
        
