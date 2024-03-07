import sys
input = sys.stdin.readline
x=input().strip()
cnt = 0
for i in x:
    if(i=='@'):
        cnt += 1
    elif i=='(':
        print(cnt, end=' ')
        cnt = 0
print(cnt)
