def solution(brown, yellow):
    # for x in range(3, brown-2):
    for x in range(3, int((brown+yellow) ** 0.5) + 1): #약수쌍의 절반만 확인하면 됨
        if (brown - x*2)%2 == 0:
            y = (brown - x*2)//2 + 2
            if (x-2) * (y-2) == yellow:
                if x > y:
                    return [x,y]
                else:
                    return [y,x]
