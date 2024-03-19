def solution(order):
    from collections import deque
    import sys
    input = sys.stdin.readline
    q = deque() #보조컨테이너
    answer = 0
    container = 1
    while True:
        #찾는 값이 보조컨테이너에 존재한다면
        if q and q[-1] == order[answer]:
            q.pop()
            answer += 1
        #찾는 값이 컨테이너에 존재한다면
        elif container <= len(order) and container == order[answer]:
            answer += 1
            container += 1
        #컨테이너, 보조 컨테이너 꺼낼 수 있는 값이 찾는 값이 아니라면
        else:
            if container <= len(order):
                q.append(container)
                container += 1
            else:
                break
    
    return answer

