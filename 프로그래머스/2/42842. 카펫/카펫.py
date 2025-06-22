def solution(brown, yellow):
    for i in range(3, brown-2):
        x = i
        if (brown - x*2)%2 == 0:
            y = (brown - x*2)//2 + 2
            if (x-2) * (y-2) == yellow:
                if x > y:
                    return [x,y]
                else:
                    return [y,x]
