def solution(num_list):
    answer = 0
    for i in num_list:
        x = 0
        while i > 1:
            if i % 2!= 0:
                i -= 1
            i /= 2
            x += 1
        answer += x
    return answer