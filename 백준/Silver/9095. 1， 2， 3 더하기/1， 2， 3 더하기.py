import sys
input = sys.stdin.readline
n=int(input())
dp = [0] * 11
max = 3

def DFS(x):
    global max
    if x==0 or x==1:
        return 1
    elif x==2:
        return 2

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(max,x+1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    max = x
    return dp[x]


for _ in range(n):
    print(DFS(int(input())))