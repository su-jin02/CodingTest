import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append(n)
visited[n] = 0
while q:
    x = q.popleft()
    if x==m:
        print(visited[x])
        break
    if 0<=x*2<=100000 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        q.append(x*2)
    if 0<=x - 1<=100000 and visited[x - 1] == -1:
        visited[x - 1] = visited[x] + 1
        q.append(x-1)
    if 0<=x + 1<=100000 and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        q.append(x+1)
