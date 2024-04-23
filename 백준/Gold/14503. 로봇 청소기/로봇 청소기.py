#
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1
res = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3) % 4
        tx = r + dx[d]
        ty = c + dy[d]

        if 0 <= tx < n and 0 <= ty < m and arr[tx][ty] == 0 and visited[tx][ty] == 0:
            visited[tx][ty] = 1
            res += 1
            r = tx
            c = ty
            flag = 1 # 청소함
            break

    if flag == 0: #네 방향 모두 청소를 할 수 없을 때
        if arr[r-dx[d]][c-dy[d]] == 1: # 후진 =  내가 가지고 있는 방향을 빼줌
            print(res)
            break
        else:
            r, c = r-dx[d], c-dy[d]