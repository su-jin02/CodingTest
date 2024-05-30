def solution(prices):
    stack = []
    x = len(prices) - 1
    answer = [0] * (x+1)
    for i in range(x+1):
        answer[i] = x-i
        while stack and prices[stack[-1]] > prices[i]:
            answer[stack.pop()] -= x-i
        stack.append(i)
    return answer