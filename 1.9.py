#1번부터 b까지 가는 경로의 수
import sys
a,b = map(int, sys.stdin.readline().split())
ch = [[0]*(a+1) for _ in range(a+1)]
n = [0] * (a + 1)

for _ in range(b):
    i, j = list(map(int, sys.stdin.readline().split()))
    ch[i][j] = 1

result = 0

def DFS(x):
    global result
    if n[x] == 1:
        return
    if x == a:
        result += 1
    else:
        for i in range(1, a + 1):
            if ch[x][i] == 1:
                n[x] = 1
                DFS(i)
                n[x] = 0

DFS(1)
print(result)
