def solution(arr):
    x = len(arr)
    y = len(arr[0])
    if x > y:
        for i in range(x):
            for _ in range(x-y):
                arr[i].append(0)
    elif x<y:
        for _ in range(y-x):
            arr.append([0]*y)
    return arr