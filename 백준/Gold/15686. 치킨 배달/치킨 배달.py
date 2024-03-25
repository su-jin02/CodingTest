from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(n, index): # n: 고른 치킨집 수 i: 고른 치킨집 번호
    global result
    num = 0
    if n == M:
        for h in house:
            hx, hy = h[0], h[1]
            dist = 2*N

            for s in select:
                sx, sy = s[0], s[1]
                tmp = abs(hx-sx) + abs(hy-sy)
                if tmp < dist:
                    dist = tmp
            num += dist

        if num < result:
            result = min(num, result)
            return

    for i in range(index, len(chick)):
        select.append(chick[i])
        dfs(n+1, i+1)
        select.pop()

chick = deque([])
house = deque([])
select = deque([])

#집과 치킨집 위치 큐에 추가
for a in range(N):
    for b in range(N):
        if arr[a][b] == 1:
            house.append((a, b))
        elif arr[a][b] == 2:
            chick.append((a, b))

result = 100000
for x in range(len(chick)):
    dfs(0, x)
print(result)