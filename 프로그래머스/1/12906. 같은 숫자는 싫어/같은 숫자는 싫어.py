def solution(arr):
    answer = []
    for i in arr:
        if answer:
            if i != answer[-1]:
                answer.append(i)
        else:
            answer.append(i)
    return answer