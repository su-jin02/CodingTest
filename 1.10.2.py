#백준1927 최소힙
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
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)

