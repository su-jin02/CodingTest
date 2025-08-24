from collections import deque
def solution(board):
    answer = -1
    len_x = len(board[0])
    len_y = len(board)    
    start_x, start_y, goal_x, goal_y = 0,0,0,0
    visited = [[0] * (len_x+1) for _ in range(len_y+1)]
    for i in range(len_y):
        for j in range(len_x):
            if board[i][j] == 'D':
                visited[i][j] = 2
            elif board[i][j] == 'R':
                start_x = j
                start_y = i
            elif board[i][j] == 'G':
                goal_x = j
                goal_y = i
                
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    q = deque([(start_x, start_y,0)])
    while q:
        tx , ty,res = q.popleft()
        if tx == goal_x and ty == goal_y:
            return res
        visited[ty][tx] = 1
        for i in range(4):
            x = tx + dx[i]
            y = ty + dy[i]
            
            if 0<=x<len_x and 0<=y<len_y and visited[y][x] == 0:
                while True: #직진 
                    if 0<=x+dx[i]<len_x and 0<=y+dy[i]<len_y and visited[y+dy[i]][x+dx[i]] != 2:
                        x += dx[i]
                        y += dy[i]
                    else:
                        break
                if visited[y][x] != 1:
                    q.append((x,y,res+1))       
    return -1