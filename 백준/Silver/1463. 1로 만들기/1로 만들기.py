import sys
input = sys.stdin.readline
x=int(input())

#내가 짠 코드
# dy=[1000]*(x+1)
# dy[x]=0
# def DFS(n):
#     if n <= 1:
#         return
#     if n % 3 == 0 and dy[n//3] > dy[n] + 1:
#         dy[n//3] = dy[n] + 1
#         DFS(n//3)
#     if n % 2 == 0 and dy[n//2] > dy[n] + 1:
#         dy[n//2] = dy[n] + 1
#         DFS(n // 2)
#
#     if dy[n - 1] > dy[n] + 1:
#         dy[n - 1] = dy[n] + 1
#         DFS(n - 1)
# DFS(x)
# print(dy[1])

# 풀이 참고
dp = {1: 0}
def cal(n):
    if n in dp.keys():
        return dp[n]
    if (n % 3 == 0) and (n % 2 == 0):
        dp[n] = min(cal(n // 3) + 1, cal(n // 2) + 1)
    elif n % 3 == 0:
        dp[n] = min(cal(n // 3) + 1, cal(n - 1) + 1)
    elif n % 2 == 0:
        dp[n] = min(cal(n // 2) + 1, cal(n - 1) + 1)
    else:
        dp[n] = cal(n - 1) + 1

    return dp[n]

print(cal(x))