import sys, math
input = sys.stdin.readline
n = int(input())

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)): #에라토스테네스의 체
        if x % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if isPrime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)