def solution(a, b):
    x = str(a) + str(b)
    y = str(b) + str(a)
    if int(x) > int(y):
        return int(x)
    else:
        return int(y)