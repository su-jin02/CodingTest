#겹치는 공간 뺴는 방식으로 푸려다.. 푸는 방식을 검색해봄ㅜ
import sys
input = sys.stdin.readline
n=int(input())
res = [[0]*101 for _ in range(101)]
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            res[i][j] = 1

count = 0
for i in range(1,101):
    for j in range(1,101):
        if res[i][j] == 1:
            count += 1
print(count)
