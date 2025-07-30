from collections import deque
def solution(game_board, table):
    n = len(game_board)
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited_game_board = [[0] * len(game_board) for _ in range(n)]
    visited_table = [[0] * len(game_board) for _ in range(n)]
    # bfs 빈칸 찾기
    q = deque()
    blank = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and visited_game_board[i][j] == 0:
                visited_game_board[i][j] = 1
                q.append([i, j])
                temp = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        tx = x + dx[k]
                        ty = y + dy[k]
                        if 0 <= tx < n and 0 <= ty < n and visited_game_board[tx][ty] == 0 and game_board[tx][ty] == 0:
                            visited_game_board[tx][ty] = 1
                            q.append([tx, ty])
                            temp.append((tx, ty))
                blank.append(temp)
    # bfs 도형찾기
    q = deque()
    shape = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and visited_table[i][j] == 0:
                visited_table[i][j] = 1
                q.append([i, j])
                temp = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        tx = x + dx[k]
                        ty = y + dy[k]
                        if 0 <= tx < n and 0 <= ty < n and visited_table[tx][ty] == 0 and table[tx][ty] == 1:
                            visited_table[tx][ty] = 1
                            q.append([tx, ty])
                            temp.append((tx, ty))
                shape.append(temp)

    # 정규화
    def normalize(cells):
        xs = [x for x,y in cells]
        ys = [y for x,y in cells]
        minx, miny = min(xs), min(ys)
        return sorted([(x-minx, y-miny) for x,y in cells])

    # 비교하기
    rots = [
    lambda x,y: ( x,  y),
    lambda x,y: ( y, -x),
    lambda x,y: (-x, -y),
    lambda x,y: (-y,  x),
]
    
    used_shape = [0] * len(shape)
    for blank_i in blank:
        norm_blank = normalize(blank_i)
        for j in range(len(shape)):
            found = False
            if used_shape[j] == 0 and len(blank_i) == len(shape[j]):
                shape_j = shape[j]
                for rot in rots:
                    rotated = [rot(x, y) for x, y in shape_j]
                    if normalize(rotated) == norm_blank:
                        answer += len(blank_i)
                        used_shape[j] = 1
                        found = True
                        break
            if found:
                break 
    return answer