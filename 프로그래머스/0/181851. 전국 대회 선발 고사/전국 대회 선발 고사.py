def solution(rank, attendance):
    answer = []
    for i,j in enumerate(attendance):
        if j == 1:
            answer.append([rank[i],i])
    answer.sort()
    return answer[0][1]*10000  + answer[1][1]*100 + answer[2][1]