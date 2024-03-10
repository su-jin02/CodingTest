#조합으로 해결
import sys, math
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    i,j = map(int, input().split())
    print(math.comb(j, i))