def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
        if len(answer) == k:
            break
    
    x = k - len(answer)
    
    # k보다 작으면 -1로 채움
    if x > 0:
        answer.extend([-1] * x)
    
    return answer