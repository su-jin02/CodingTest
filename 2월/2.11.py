#백준12099 정렬
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
menu = [list(map(int, input().split())) for _ in range(n)]
menu.sort()
day = [list(map(int, input().split())) for _ in range(m)]

def binary(target):
    left, right = 0, len(menu) - 1
    while left <= right:
        mid = (left + right) // 2
        if menu[mid][0] == target:
            return mid
        elif menu[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

for spi1, spi2, swe1, swe2 in day:
    res = 0
    for i in menu[binary(spi1):binary(spi2)]:
        if swe1 <= i[1] <= swe2:
            res += 1
    print(res)