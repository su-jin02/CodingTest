# 강의섹션7. 피자 배달 거리(DFS)
import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
ch= [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
res = 214700
house=[]
pizza=[]

for i in range(n):
    for j in range(n):
        if ch[i][j] == 1:
            house.append([i,j])
        elif ch[i][j] == 2:
            pizza.append([i,j])

comb = combinations(pizza, m)
for c in comb:
    total = 0
    for hs in house:
        dis = 214700
        for pz in c:
            cnt = abs(hs[0] - pz[0]) + abs(hs[1] - pz[1])
            if dis > cnt:
                dis = cnt
        total += dis
    if res > total:
        res = total

print(res)
