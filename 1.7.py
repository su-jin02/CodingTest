#1부터 x까지의 번호가 적힌 구슬을 y개 뽑는 경우의 수
import sys
n,m = map(int, sys.stdin.readline().split())
result = 0

def DFS(L, s):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i + 1)


res = [0] * (n + 1)
cnt = 0
DFS(0, 1)
print(cnt)