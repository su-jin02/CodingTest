def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        x = -1
        for i in range(s,e+1):
            if arr[i] > k:
                if x == -1:
                    x = arr[i]
                else:
                    if x > arr[i]:
                        x = arr[i]
        answer.append(x)
    return answer