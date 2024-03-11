import sys
input = sys.stdin.readline
n = int(input())
dp = [[0,0,0] for _ in range(n)]
i,j,k = map(int, input().split())
dp[0][0] = i
dp[0][1] = j
dp[0][2] = k
for x in range(1,n):
    i,j,k = map(int, input().split())
    dp[x][0] = min(dp[x-1][1], dp[x-1][2]) + i
    dp[x][1] = min(dp[x-1][0], dp[x-1][2]) + j
    dp[x][2] = min(dp[x-1][0], dp[x-1][1]) + k

print(min(dp[n-1]))