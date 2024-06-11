def solution(name):
    len_name = len(name)
    answer = 0
    move = len_name - 1
    for i in range(len_name):
        if (name[i] != 'A'):
            cal = ord(name[i])
            answer += min(91-cal, cal-65)

        j = i + 1
        while j < len_name and name[j] == 'A':
            j += 1
        # 우측이동 후 좌측으로 이동, 좌측이동 후 우측 이동인지
        move = min(move, i + i + len_name - j, (len_name - j) * 2 + i)
        
    return answer + move