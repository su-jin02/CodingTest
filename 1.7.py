#1부터 x까지의 번호가 적힌 구슬을 y개 뽑는 경우의 수
import sys
x,y = map(int, sys.stdin.readline().split())
result = 0

def DFS(n,m):  #(가지 뻗는 첫번째 수, 레벨)
    global ch, result
    if m == y:
        for i in ch:
            print(i, end=' ')
        print()
        result += 1
    else:
        for i in range(n,x+1):
            ch[m] = i
            DFS(i+1,m+1)

ch= [0]*y
DFS(1,0)
print(result)