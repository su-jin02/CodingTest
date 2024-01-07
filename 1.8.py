#a개의 정수 중 b개를 뽑아 k 배수 조합 개수 출력
import sys
a,b = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
k= int(sys.stdin.readline())
result = 0

def DFS(n,m, sum):  #(가지 뻗는 첫번째 수, 뽑은 개수, 누적합)
    global ch, result
    if m == b:
        if sum % k == 0:
            result += 1
    else:
        for i in range(n,a):
            DFS(i+1, m+1, sum+lst[i])

DFS(0,0,0)
print(result)
