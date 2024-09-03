def solution(my_string, alp):
    new_string = list(my_string)
    for i in range(len(new_string)):
        if new_string[i] == alp:
            new_string[i] = alp.upper()
    return ''.join(new_string)