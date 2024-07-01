def solution(a, b):
    if a % 2 == 0:
        if b % 2 == 0: #(짝,짝)
            return abs(a-b)
        else:#(짝,홀)
            return 2*(a+b)
    else: 
        if b % 2 == 0: #(홀,짝)
            return 2*(a+b)
        else:#(홀,홀)
            return pow(a,2)+pow(b,2)
