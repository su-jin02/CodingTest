import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1], reverse=True)
time = arr[0][1]

for i,j in arr:
    if j<time:
        time = j-i
    else:
        time -= i

if time<0:
    print(-1)
else:
    print(time)