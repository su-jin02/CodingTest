import sys, math
input = sys.stdin.readline

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)): #에라토스테네스의 체
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

n = int(input())
while True:
    if isPalindrome(n) and isPrime(n):
        print(n)
        break
    n += 1

