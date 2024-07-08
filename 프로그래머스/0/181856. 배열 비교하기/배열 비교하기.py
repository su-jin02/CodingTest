def solution(arr1, arr2):
    x = len(arr1)
    y = len(arr2)
    if x==y:
        a = sum(arr1)
        b = sum(arr2)
        if a==b:
            return 0
        elif a>b:
            return 1
        else:
            return -1
    elif x>y:
        return 1
    else: 
        return -1
    return 