#집합을 두 개의 부분집합으로 나누었을때 두 부분집합의 원소의 합이 같을 경우 존재 여부
import sys
def DFS(n):
    if n == x:
        a = 0
        b = 0
        for i in range(x):
            if (ch[i] == 1):
                a += lst[i]
            else:
                b += lst[i]
        if a==b:
            print('YES')
            exit()
    else:
        ch[n] = 1
        DFS(n+1)
        ch[n] = 0
        DFS(n+1)

x = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
ch = [0] * (x)
DFS(0)
print('NO')

# --------------------------
# => 위는 전과 같은 방식으로 품
# 해설풀이
# DFS(현재 트리 level, 현재까지 부분집합 합)
# => 기존 방식은 부분집합 합을 비교하기 위한 또 한번의 loop를 돌지만 해설은 탐색을 하며 sum을 계산할 수 있음
# --------------------------

def DFS(level, sum):
    if sum > total/2:
        return   #!!시간복잡도를 줄이기위해 넣어줘야함!!
    if level == x:
        if sum == total-sum:
            print('YES')
            exit()
    else:
        DFS(level+1, sum +lst[level])
        DFS(level+1, sum)

x = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
total = sum(lst)
DFS(0,0)
print('NO')