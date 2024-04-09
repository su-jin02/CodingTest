def solution(lottos, win_nums):
    answer = []
    count = 0 #0개수
    res = 0 #일치하는 개수
    for i in lottos:
        if i==0:
            count += 1
        elif i in win_nums:
            res += 1
    if res + count < 2 :
        answer = [6,6]
    else:
        answer.append(7-(res+count))
        if res < 2:
            answer.append(6)
        else:
            answer.append(7-res)

    return answer