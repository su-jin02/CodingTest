import sys
input = sys.stdin.readline
n = int(input())
dp = []
for x in range(n):
    dp.append(list(map(int, input().split())))
    if x>0:
        dp[x][0] += min(dp[x-1][1], dp[x-1][2])
        dp[x][1] += min(dp[x-1][0], dp[x-1][2])
        dp[x][2] += min(dp[x-1][0], dp[x-1][1])

print(min(dp[-1]))