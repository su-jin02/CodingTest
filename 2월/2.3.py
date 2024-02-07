# 강의섹션8. 최대점수 구하기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dy=[0]*(m+1) #해당 인덱스 시간동안 풀 수 있는 최대점수
for i in range(n):
    score, time = map(int, input().split())
    for j in range(time, m+1):
        dy[j] = max(dy[j], dy[j-time]+score)

print(dy[m])
