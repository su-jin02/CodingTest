# 강의섹션8. 동전교환
import sys
input = sys.stdin.readline
n=int(input())
coin=list(map(int, input().split()))
m=int(input())
dy=[1000]*(m+1);
dy[0]=0
for i in range(n):
    for j in range(coin[i], m+1):
        dy[j]=min(dy[j], dy[j-coin[i]]+1)
print(dy[m])
