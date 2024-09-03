#풀이 참고
import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
money = int(input())
if sum(arr) <= money:
    print(max(arr))
else:
    start, end = 0, max(arr)
    total = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            total += min(mid, i)

        if total <= money:
            start = mid + 1
        else:
            end = mid - 1
    print(end)

