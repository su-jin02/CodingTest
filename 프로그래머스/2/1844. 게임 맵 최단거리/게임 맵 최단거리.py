from collections import deque

def solution(maps):
    answer = -1
    len_x = len(maps)
    len_y = len(maps[0])

    q = deque([[0, 0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        if x == len_x - 1 and y == len_y - 1:
            answer = maps[x][y]
            break
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < len_x and 0 <= ty < len_y:
                if maps[tx][ty] == 1:
                    maps[tx][ty] = maps[x][y] + 1
                    q.append([tx, ty])
    return answer