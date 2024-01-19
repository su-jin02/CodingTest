# 강의섹션7. 동전 분배하기
import sys
input = sys.stdin.readline
x = int(input())
ch = [int(input()) for _ in range(x)]
money = [0]*3
res = 100000

def DFS(n):
    global res
    if n == x:
        if len(set(money)) == 3:
            if res > max(money)-min(money):
                res = max(money)-min(money)
        return
    else:
        for i in range(3):
            money[i] += ch[n]
            DFS(n+1)
            money[i] -= ch[n]

DFS(0)
print(res)