from collections import deque
def solution(ingredient):
    q = deque()
    answer = 0
    for i in ingredient:
        if i==1: #빵일때
            if len(q)>=3:
                if q[-1] == 3:
                    if q[-2] == 2:
                        if q[-3] == 1:
                            answer += 1
                            q.pop()
                            q.pop()
                            q.pop()
                            continue
        q.append(i)

    return answer
