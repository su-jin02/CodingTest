#1부터 x까지의 번호가 적힌 구슬을 y번 중복을 허락해서 뽑는 경우의 수
import sys
x,y = map(int, sys.stdin.readline().split())
result = 0

def DFS(a):
    global e, result
    if(a == y):
        for i in e:
            print(i, end=' ')
        print()
        result += 1
    else:
        for i in range(x):
            e[a] = i+1
            DFS(a+1)

e = [0]*y
DFS(0)
print(result)