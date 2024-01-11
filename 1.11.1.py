#백준11279 최대힙
import sys, heapq
heap = []
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = int(input())
    if a == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-a, a))
