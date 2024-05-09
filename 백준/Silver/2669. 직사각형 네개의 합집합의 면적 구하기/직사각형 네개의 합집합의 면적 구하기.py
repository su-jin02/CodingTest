import sys
input = sys.stdin.readline

visited = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2,1):
        for j in range(y1, y2, 1):
            if visited[j][i] == 0:
                visited[j][i] = 1
                result += 1
print(result)
