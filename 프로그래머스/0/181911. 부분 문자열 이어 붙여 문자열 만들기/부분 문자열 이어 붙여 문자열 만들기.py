def solution(my_strings, parts):
    answer = ''
    for i,(j,k) in enumerate(parts):
        answer += my_strings[i][j:k+1]
    return answer