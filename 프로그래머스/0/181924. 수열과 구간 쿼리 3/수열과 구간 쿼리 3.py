def solution(arr, queries):
    for i,j in queries:
        x = arr[i]
        arr[i] = arr[j]
        arr[j] = x
    return arr