from collections import deque

def solution(word):
    dic = ['A', 'E', 'I', 'O', 'U']
    diction = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    dq = deque([])
    answer = 0
    prev = 0
    while "".join(dq) != word:
        print(dq)
        if len(dq) == 5:
            x = dq.pop()
            if x == 'U':
                while True:
                    y = dq.pop()
                    if y != 'U':
                        prev = diction[y]+1
                        dq.append(dic[prev])
                        answer += 1
                        prev = 0
                        break
            else:
                prev += 1
                dq.append(dic[prev])
                answer += 1
        else:
            dq.append(dic[prev])
            answer += 1
    return answer