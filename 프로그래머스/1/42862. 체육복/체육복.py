def solution(n, lost, reserve):
    rest = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            rest.append(i)
    rest.sort()
    for i in rest:
        if i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            n -= 1
    return n