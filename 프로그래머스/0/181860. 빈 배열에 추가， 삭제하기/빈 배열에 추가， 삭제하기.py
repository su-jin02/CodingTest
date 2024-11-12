def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i] == 1:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                del answer[-1]
    return answer
