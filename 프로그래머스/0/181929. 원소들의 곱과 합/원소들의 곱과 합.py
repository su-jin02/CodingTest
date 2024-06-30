def solution(num_list):
    x = 0
    y = 1
    for i in num_list:
        x += i
        y *= i
    if y > pow(x,2):
        return 0
    else:
        return 1
