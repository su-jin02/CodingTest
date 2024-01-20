# 강의섹션7. 송아지찾기
import sys
from collections import deque
input = sys.stdin.readline
x,y = map(int, input().split(' '))
ch= [-1,1,5]
maxx = 10000
res = [0] * (maxx+1) #거리
visited = [0] * (maxx+1) #방문여부
q = deque()
q.append(x)
visited[x] = 1

while q:
    n = q.popleft()
    if(n == y):
        print(res[y])
        break

    for i in ch:
        if 0 < n+i <= maxx:
            if visited[n+i] == 0:
                q.append(n+i)
                visited[n+i] = 1
                res[n+i] = res[n]+1
