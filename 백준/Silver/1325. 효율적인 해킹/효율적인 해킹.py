# bfs 탐색을 통해 가장 많은 노드를 탐색한 노드를 출력
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    cnt = 0

    visited = [False] * (n + 1)
    visited[x] = True

    while q:
        num = q.popleft()
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt


result = []
for i in range(1, len(graph)):
    result.append(bfs(i))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i + 1)

