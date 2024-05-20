def solution(numbers, target):
    answer = 0
    def dfs(sum, n):
        nonlocal answer
        if n == len(numbers):
            if sum == target:
                answer += 1
            return
        dfs(sum+numbers[n], n+1)
        dfs(sum-numbers[n], n+1)
    dfs(0,0)
    return answer

