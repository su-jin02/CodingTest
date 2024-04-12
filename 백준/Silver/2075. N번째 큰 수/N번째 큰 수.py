import sys, heapq
input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    num = map(int, input().split())
    for i in num:
        if len(h) < n:
            heapq.heappush(h, i)
        else:
            if h[0] < i:
                heapq.heappop(h)
                heapq.heappush(h, i)
print(h[0])
