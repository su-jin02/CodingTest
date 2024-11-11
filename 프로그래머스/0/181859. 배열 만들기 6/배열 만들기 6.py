def solution(arr):
    stk = []
    x = len(arr)
    i = 0
    while i < x:
        if not stk:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                del stk[-1]
            else:
                stk.append(arr[i])
        i += 1
    if not stk:
        return [-1]
    return stk