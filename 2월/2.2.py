# 강의섹션8. 가장 높은 탑 쌓기
import sys
input = sys.stdin.readline
n=int(input())
board= [list(map(int, input().split())) for _ in range(n)]
board.sort(key=lambda x: x[0], reverse=True) #밑면 넓이로 내림차순 정렬
dp = [0] * n
dp[0] = board[0][1]
res = 0

for i in range(1,n):
    max_h = 0
    for j in range(i-1,-1,-1):
        if board[j][2] > board[i][2]: #무게 비교
            if dp[j] > max_h:
                max_h = dp[j]
    dp[i] = max_h + board[i][1]
    res = max(res, dp[i])
print(res)