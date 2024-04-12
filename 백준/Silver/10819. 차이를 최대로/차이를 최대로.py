import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
p = list(permutations(board, n))
res = 0
for i in p:
    num = 0
    for j in range(n - 1):
        num += abs(i[j] - i[j + 1])
    res = max(res, num)
print(res)
