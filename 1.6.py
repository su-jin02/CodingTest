#가장 적은 수의 동전으로 거스름돈 주기
import sys
result = 10000

def DFS(n,sum): #(동전개수, 동전합)
    global result
    if n>result or sum>b: #이미 나온 최솟값보다 개수가 커지거나 구하려는 값을 넘어가면 탐색 중지
        return

    if(sum == b):
        if(result > n):
            result = n
    else:
        for i in lst:
            DFS(n+1, sum+i)


a= int(sys.stdin.readline())
lst= list(map(int, sys.stdin.readline().split()))
b= int(sys.stdin.readline())
lst.sort(reverse=True)
print(lst)
DFS(0,0)
print(result)