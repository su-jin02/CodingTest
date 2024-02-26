import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
x=int(input())
dy=[1000]*(x+1)
dy[x]=0

def DFS(n):
    if n <= 1:
        return
    if n % 3 == 0 and dy[n//3] > dy[n] + 1:
        dy[n//3] = dy[n] + 1
        DFS(n//3)
    if n % 2 == 0 and dy[n//2] > dy[n] + 1:
        dy[n//2] = dy[n] + 1
        DFS(n // 2)

    if dy[n - 1] > dy[n] + 1:
        dy[n - 1] = dy[n] + 1
        DFS(n - 1)

DFS(x)
print(dy[1])