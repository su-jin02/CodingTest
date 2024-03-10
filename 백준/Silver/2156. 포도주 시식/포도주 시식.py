import sys
input = sys.stdin.readline
n = int(input())
ch = list(int(input()) for _ in range(n))
dp = [0] * (n+2)
dp[0] = ch[0]

if n>1 : #index error 방지
    dp[1] = ch[0] + ch[1]
if n>2:
    dp[2] = max(dp[1], ch[0]+ch[2], ch[1]+ch[2])
for i in range(3,n):
    dp[i] = max(dp[i-1] , dp[i-2] + ch[i], dp[i-3] + ch[i-1] + ch[i])
    # 현재 잔까지의 최대값을 구함
    # 1. 현재 잔을 마시지 않을 때 = i-1번째의 최대값
    # 2. 현재 잔을 마실 때
    # 2-1. xoo로 마실 때  = i-3번째 최대값 + ch[i-1] + ch[i]
    # 2-2. oxo로 마실 때 = i-2번째 최대값 + ch[i] (xxo의 케이스를 포함)

print(dp[n-1])