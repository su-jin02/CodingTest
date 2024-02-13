#백준12099 이진탐색
import sys
import bisect
input = sys.stdin.readline
n, m = map(int, input().split())

menu = []
menu1=[]
for i in range(0,n):
    x, y = map(int,input().split())
    menu.append([x,y])
    menu1.append(x)
menu.sort()
menu1.sort()

def left_binary(target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if menu[mid][0] == target:
            return mid
        elif menu[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def right_binary(target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if menu[mid][0] == target:
            return mid + 1 #우측이면 범위를 하나 더 추가해줘야함
        elif menu[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

for i in range(m):
    spi1, spi2, swe1, swe2 = map(int, input().split())
    res = 0
    # for j in range(left_binary(spi1), right_binary(spi2)): #만든 함수 사용
    for j in range(bisect.bisect_left(menu1,spi1), bisect.bisect_left(menu1, spi2+1)): #라이브러리 사용
        if swe1 <= menu[j][1] <= swe2:
            res += 1
    print(res)