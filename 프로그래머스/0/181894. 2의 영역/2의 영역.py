def solution(arr):
    try:
        x = arr.index(2)
        y = len(arr) - arr[::-1].index(2)
        return arr[x:y]
    except ValueError:
        return [-1]