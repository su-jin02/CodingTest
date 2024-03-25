#스타트와 링크
import sys
input = sys.stdin.readline
n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]
result = 100
visited = [0]*n

def team(a,index):
    global result
    if a == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += power[i][j]
                elif not visited[i] and not visited[j]:
                    link += power[i][j]
        result = min(result,abs(start-link))
        return
    else:
        for x in range(index,n):
            if visited[x] == 0:
                visited[x] = 1
                team(a+1,x+1)
                visited[x] = 0

team(0,0)
print(result)