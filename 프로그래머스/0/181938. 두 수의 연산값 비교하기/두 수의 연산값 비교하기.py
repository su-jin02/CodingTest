def solution(a, b):
    answer = 0
    x = str(a) + str(b)
    y = 2*a*b
    x = int(x)
    if x<y:
        answer = y
    else:
        answer = x
    return answer