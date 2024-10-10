# 강의섹션8. 최대 부분 증가수열
#수정31
import sys
input = sys.stdin.readline
a = int(input())
ch = list(map(int, input().split()))
dy = [0] * a
dy[0] = 1
res = 0
for i in range(1, a):
    for j in range(0, i):
        if ch[i] > ch[j] and dy[i] < dy[j]:
            dy[i] = dy[j]
    dy[i] += 1
    if res < dy[i]:
        res = dy[i]

print(res)
