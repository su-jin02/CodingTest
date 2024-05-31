def solution(storey):
    answer = 0
    while storey != 0:
        x = storey%10
        if x > 5:
            answer += 10-x
            storey += 10-x
        elif x<5:
            answer += x
        else: #ex) 485의 경우 12가 아닌 11
            y = int(storey/10)%10
            if y+1 >5:
                storey += 5
            answer += 5

        storey = int(storey/10)

    return answer