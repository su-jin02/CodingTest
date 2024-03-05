def solution(n):
    answer = 0
    dy = [0] * (n+2)
    dy[1] = 1
    dy[2] = 2
    
    for i in range(3,n+1):
        dy[i] = dy[i-1] + dy[i-2]
    
    answer = dy[n] % (1234567)
    return answer
