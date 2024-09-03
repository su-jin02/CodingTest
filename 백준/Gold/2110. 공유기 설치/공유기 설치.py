import sys
input = sys.stdin.readline
n, c = map(int, input().split())
board = [int(input()) for _ in range(n)]
board.sort()

start = 1
end = board[-1] - board[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    current = board[0]
    count = 1

    for i in range(1, len(board)):
        if board[i] >= current + mid:
            count += 1
            current = board[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)