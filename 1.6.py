import sys
result = 1000

def DFS(n,m):
    global result
    if (m >= b):
        if(m == b):
            result = min(result, n)


    else:
        for i in lst:
            if(n+1 < result):
                DFS(n+1,m+i)


a= int(sys.stdin.readline())
lst= list(map(int, sys.stdin.readline().split()))
b= int(sys.stdin.readline())
lst.sort(reverse=True)
DFS(0,0)
print(result)