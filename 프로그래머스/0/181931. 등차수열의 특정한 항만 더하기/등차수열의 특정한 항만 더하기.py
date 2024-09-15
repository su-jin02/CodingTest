def solution(a, d, included):
    answer = []
    res = 0
    for i in range(len(included)):
        answer.append(a + d*i)
    print(answer)
    for i in range(len(included)):
        if included[i] == 1:
            res += answer[i]
    return res