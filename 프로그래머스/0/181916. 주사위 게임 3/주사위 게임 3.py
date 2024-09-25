def solution(a, b, c, d):
    x = [a,b,c,d]
    x.sort()
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    # 4개 숫자 동일
    if a == d:
        return 1111*a
    # 3개 숫자 동일
    elif a == c:
        return pow(10*a+d,2)
    elif b == d:
        return pow(10*b+a,2)
    #2개 숫자 동일
    elif a == b:
        if c == d: #쌍으로 동일
            return (a+c)*abs(a-c)
        else:
            return c*d
    elif b == c:
        return a*d
    elif c == d:
        return a*b
    #다 다름
    else:
        return a
        
        