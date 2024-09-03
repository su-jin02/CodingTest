def solution(my_string, m, c):
    answer = ''
    x = c-1
    while True:
        answer += my_string[x]
        x += m
        if x >= len(my_string):
            break      
        
    return answer