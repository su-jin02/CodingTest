import sys
input = sys.stdin.readline
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort(reverse= True)
res = 0
for i in range(1,n+1):
    res = max(res, num[i-1]*i)
print(res)