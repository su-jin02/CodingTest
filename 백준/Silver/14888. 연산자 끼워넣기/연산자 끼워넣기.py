import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split())) # +,-,*,/

min_res = pow(10,9)
max_res = -pow(10,9)
def calculate(res, index):
    global min_res, max_res
    if index == n:
        min_res = min(min_res, res)
        max_res = max(max_res, res)
        return

    for i in range(4):
        if cal[i] == 0:
            continue
        else:
            if i==0:
                cal[i] -= 1
                calculate(res+num[index], index+1)
                cal[i] += 1
            elif i==1:
                cal[i] -= 1
                calculate(res - num[index], index + 1)
                cal[i] += 1
            elif i==2:
                cal[i] -= 1
                calculate(res * num[index], index + 1)
                cal[i] += 1
            elif i==3:
                cal[i] -= 1
                if res >= 0:
                    calculate(res // num[index], index + 1)
                else:
                    calculate(abs(res) // num[index] * (-1), index + 1)
                cal[i] += 1

calculate(num[0], 1)
print(max_res)
print(min_res)