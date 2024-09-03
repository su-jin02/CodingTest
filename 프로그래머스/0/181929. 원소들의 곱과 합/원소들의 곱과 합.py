def solution(num_list):
    x=1
    y=pow(sum(num_list),2)
    for i in num_list:
        x *= i
    if x < y:
        return 1
    else:
        return 0