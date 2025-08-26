def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        temp = 0
        for j in range(i+1, len(prices)):
            temp += 1
            if prices[i] > prices[j]:
                break
        answer.append(temp)
    answer.append(0)
    return answer