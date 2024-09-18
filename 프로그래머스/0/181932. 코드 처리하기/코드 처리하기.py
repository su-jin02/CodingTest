def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if mode == 0 and i % 2 == 0:
                ret+= code[i]
            if mode == 1 and i % 2 != 0:
                ret+= code[i]
    if ret == '':
        ret = "EMPTY"
    return ret