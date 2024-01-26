# 강의섹션7. 단지 번호 붙이기
import sys
from collections import deque
input = sys.stdin.readline
a = int(input())
ch= [list(map(int, input().strip())) for _ in range(a)]
res = 0
res_list = []
q = deque()
dx=[-1, 0, 0, 1]
dy=[0, 1, -1, 0]

def canMove(x, y):
    if x < 0 or x > a-1:
        return False
    if y < 0 or y > a-1:
        return False
    return True

for i in range(a):
    for j in range(a):
        if(ch[i][j] == 1):
            q.append([i,j])
            ch[i][j] = 0
            res_list.append(1)
            while q:
                x, y = q.popleft()
                for i in range(4):
                    tx = x + dx[i]
                    ty = y + dy[i]
                    if canMove(tx, ty) and ch[tx][ty] == 1:
                        ch[tx][ty] = 0
                        res_list[res] += 1
                        q.append([tx, ty])
            res += 1

print(res)
res_list.sort()
for i in res_list:
    print(i)