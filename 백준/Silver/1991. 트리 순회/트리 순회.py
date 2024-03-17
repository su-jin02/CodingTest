import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
graph = {}
for _ in range(n):
    a,b,c = map(str, input().split())
    graph[a] = [b,c]

#전위순위
q = deque('A')
def front():
    while q:
        x = q.popleft()
        print(x,end='')
        for i in range(2):
            if graph[x][i] == '.':
                continue
            q.append(graph[x][i])
            front()
front()
print()

#중위순위
q = deque('A')
def middle(x):
    for i in range(2):
        if graph[x][i] == '.':
            if not q:
                break
            print(q.pop(), end='')
            continue
        q.append(graph[x][i])
        middle(graph[x][i])
middle('A')
print()

#후위순위
q = deque('A')
def end(x):
    for i in range(2):
        if graph[x][i] == '.':
            continue
        q.append(graph[x][i])
        end(graph[x][i])
    print(q.pop(), end='')
end('A')
