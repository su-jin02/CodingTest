def solution(arr):
    i = 0
    while True:
        if len(arr) > pow(2,i):
            i += 1
            continue
        elif len(arr) == pow(2,i):
            return arr
        else:
            for _ in range(pow(2,i)-len(arr)):
                arr.append(0)
            return arr