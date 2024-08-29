def solution(myString):
    answer = []
    x = 0
    for i in myString:
        if i == 'x':
            answer.append(x)
            x = 0
        else:
            x += 1
    answer.append(x)
    return answer