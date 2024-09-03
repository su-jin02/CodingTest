import sys
input = sys.stdin.readline
n,m = map(int, input().split())
num = list(int(input()) for _ in range(n))
dp = [0]*(m+2)
dp[0] = 1

for x in num:
    for i in range(x,m+1):
        dp[i] += dp[i-x]

print(dp[m])