import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(x, num):
  num += 1
  visited[x] = True

  if x == b:
    result.append(num)
    return

  for i in graph[x]:
    if not visited[i]:
      dfs(i, num)

dfs(a, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)