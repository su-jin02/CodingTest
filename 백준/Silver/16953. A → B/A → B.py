import sys
input = sys.stdin.readline
n,m = map(int, input().split())

def cal(x, count):
    if x>m:
        return
    elif x==m:
        print(count)
        exit()
    else:
        cal(x*2,count+1)
        cal(int(str(x)+'1'), count+1)

cal(n,1)
print(-1)