def solution(myString, pat):
    x= ''
    for i in myString:
        if i == 'A':
            x += 'B'
        elif i == 'B':
            x += 'A'
    if pat in x:
        return 1
    else:
        return 0
