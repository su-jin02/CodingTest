#강의섹션7. 휴가
import sys
input = sys.stdin.readline
x = int(input())
day = [0]
money = [0]
result = 0
for _ in range(x):
    a,b = map(int, input().split())
    day.append(a)
    money.append(b)

def DFS(n, Tmoney):
    global result
    if n > x+1:
        return
    if n == x+1:
        if result < Tmoney:
            result = Tmoney
    else:
        DFS(n+day[n], Tmoney+money[n])
        DFS(n+1, Tmoney)

DFS(1,0)
print(result)