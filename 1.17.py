#강의섹션7. 양팔저울
import sys
input = sys.stdin.readline
x = int(input())
ch = list(map(int, input().split()))
# res = [0] * sum(ch)
res = set()

def DFS(n, weight):
    global res
    if n == x:
        if weight>0:
            res.add(weight)
            # res[weight] = 1
    else:
        DFS(n+1, weight+ch[n])
        DFS(n+1, weight-ch[n])
        DFS(n+1, weight)

DFS(0,0)
print(sum(ch)- len(res))