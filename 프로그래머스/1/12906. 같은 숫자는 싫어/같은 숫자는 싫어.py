from collections import deque
def solution(arr):
    q = deque()
    for i in arr:
        if q and q[-1] == i:
            continue
        else:
            q.append(i)
    return list(q)