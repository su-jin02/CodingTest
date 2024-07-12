def solution(arr, n):
    x = len(arr)
    if x %2 != 0:
        for i in range(x):
            if i % 2 == 0:
                arr[i] += n
    else:
        for i in range(x):
            if i % 2 != 0:
                arr[i] += n
                
    return arr