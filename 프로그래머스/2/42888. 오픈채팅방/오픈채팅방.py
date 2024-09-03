def solution(record):
    answer = []
    user = {}
    for i in range(len(record)):
        x = record[i].split(' ')
        if x[0] != 'Leave':
            user[x[1]] = x[2]
        record[i] = [x[1],x[0]]

    #출력
    for name,verb in record:
        if verb == 'Enter':
            answer.append(user[name]+'님이 들어왔습니다.')
        elif verb == 'Leave':
            answer.append(user[name]+'님이 나갔습니다.')
        else:
            continue
    return answer