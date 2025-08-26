def solution(n, words):
    answer = [0,0]
    turn = 1
    speak = [0] * (n+1)
    last_word = words[0][0]
    dic = set()
    for i in words:
        speak[turn] += 1
        temp_len = len(dic)
        dic.add(i)
        if len(dic) == temp_len or last_word != i[0]:
            answer[0] = turn
            answer[1] = speak[turn]
            return answer
        last_word = i[-1]
        if turn == n:
            turn = 1
        else:
            turn += 1

    return answer