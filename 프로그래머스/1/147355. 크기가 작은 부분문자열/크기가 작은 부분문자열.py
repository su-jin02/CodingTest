def solution(t, p):
    answer = 0
    x= len(p)
    for i in range(len(t)-x+1):
        if t[i:i+x] <= p:
            answer += 1
    return answer