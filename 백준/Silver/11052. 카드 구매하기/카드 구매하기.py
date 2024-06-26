import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
dp = [0]*(n+2)
for i in range(1,n+1):
    dp[i] = card[i-1]
    for j in range(1,i):
        dp[i] = max(dp[i], dp[i-j]+card[j-1])

print(dp[n])

