import sys
input = sys.stdin.readline
n = int(input())
ch = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n):
    day, money = ch[i]
    if day + i <= n:
        dp[day+i] = max(max(dp[:i+1]) + money, dp[day+i])

print(max(dp))