import sys
input = sys.stdin.readline
m = int(input())
for _ in range(m):
    res = 1
    n = int(input())
    person = [list(map(int,input().split())) for _ in range(n)]
    person.sort()
    maxx = person[0][1]
    for i in range(1,n):
        if maxx > person[i][1]:
            maxx = person[i][1]
            res += 1
    print(res)
