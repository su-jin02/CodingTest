def solution(my_string, indices):
    str_list = list(my_string)
    for i in sorted(indices, reverse=True):
        str_list.pop(i)
    return ''.join(str_list)