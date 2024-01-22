# 강의섹션7. 사과나무
import sys
from collections import deque
input = sys.stdin.readline
a = int(input())
ch= [list(map(int, input().split())) for _ in range(a)]
visited = [[0] * a for _ in range(a)]
q = deque()

q.append([a//2,a//2])
visited[a//2][a//2] = 1
res = ch[a//2][a//2]
x=[-1,1,0,0]
y=[0,0,1,-1]
L = 0

while True:
    if L==a//2:
        break
    for _ in range(len(q)):
        n = q.popleft()
        for i in range(4):
            tx = n[0]+x[i]
            ty = n[1]+y[i]
            if visited[tx][ty] == 0:
                q.append([tx,ty])
                visited[tx][ty] = 1
                res += ch[tx][ty]
    L += 1

print(res)