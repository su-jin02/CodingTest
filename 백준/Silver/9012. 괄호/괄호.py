import sys, heapq
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    heap = []
    a = input().strip()
    for i in a:
        if i == '(':
            heapq.heappush(heap, a)
        else:
            if not heap: # ) 들어왔는데 ( 없다면 종료
                print('NO')
                break
            else:
                heapq.heappop(heap)
    else:
        if not heap:
            print('YES')
        else:
            print('NO')