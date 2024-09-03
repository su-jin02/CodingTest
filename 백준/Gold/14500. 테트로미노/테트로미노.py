#풀이 참조
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(x, y, count, total):
    global res

    if res >= total + max_val * (3 - count):
        #가지치기 : 남은 계산횟수의 블럭이 최대값일때 예상되는 값이, 현재나온 결과값보다 작으면 return
        return
    if count == 3:
        res = max(res, total)
        return
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < m and visit[tx][ty] == 0:
                if count == 1: #2개의 블럭을 선택되었을때 ㅗ모양을 만들기 위해
                    visit[tx][ty] = 1
                    dfs(x, y, count + 1, total + arr[tx][ty])
                    visit[tx][ty] = 0

                visit[tx][ty] = 1
                dfs(tx, ty, count + 1, total + arr[tx][ty])
                visit[tx][ty] = 0


visit = [([0] * m) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0
max_val = max(map(max, arr)) #arr 요소 중 최대값

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 0, arr[i][j]) #x값,y값, 계산횟수, 현재까지 결과합
        visit[i][j] = 0

print(res)