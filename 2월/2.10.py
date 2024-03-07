# 강의섹션4. 침몰하는 타이타닉
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort(reverse=True)
weight = deque(weight)
boat = 0

while weight:
    if len(weight) == 1:
        boat += 1
        break
    cnt = weight.popleft()
    if cnt + weight[-1] <= m:
        weight.pop()
    boat += 1

print(boat)

