# 입력 값을 깊이 우선 탐색 전위순회방식 출력
import sys

def DFS(n):
    if n == x+1:
        for i in range(1, x + 1):
            if (ch[i] == 1):
                print(i, end=' ')
        print()
    else:
        ch[n] = 1
        DFS(n+1)
        ch[n] = 0
        DFS(n+1)

x = int(sys.stdin.readline())
ch = [0] * (x+1)
DFS(1)
