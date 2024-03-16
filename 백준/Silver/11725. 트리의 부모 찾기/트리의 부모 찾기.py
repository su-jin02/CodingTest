import sys
from collections import deque

def func():
    input = sys.stdin.readline

    num_node = int(input())
    graph = [[] for _ in range(num_node+1)]
    for _ in range(num_node-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    tree = [0]*(num_node+1)
    queue = deque([1])
    tree[1] = 1

    while queue:
        v = queue.popleft()

        for nv in graph[v]:
            if not tree[nv]:
                tree[nv] = v
                queue.append(nv)

    for i in range(2, num_node+1):
        sys.stdout.write(f'{tree[i]}\n')
    return
func()