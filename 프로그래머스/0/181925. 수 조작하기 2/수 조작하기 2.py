def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        x = numLog[i] - numLog[i-1]
        if x == 1:
            answer += 'w'
        elif x == -1:
            answer += 's'
        elif x == 10:
            answer += 'd'
        elif x == -10:
            answer += 'a'
    return answer