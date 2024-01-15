#강의섹션7. 최대점수 구하기
import sys
input = sys.stdin.readline
x,y = map(int, input().split())
ch = []
for _ in range(x):
    a,b = map(int, input().split())
    ch.append([a,b,a/b])

ch.sort(key=lambda x:-x[2])

def DFS(n, score, time):
    if n == x:
        return score

    if(time+ch[n][1] > y):
        return DFS(n+1, score, time)
    else:
        return DFS(n+1, score+ch[n][0], time+ch[n][1])

print(DFS(0,0,0))