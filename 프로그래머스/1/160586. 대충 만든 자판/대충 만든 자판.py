def solution(keymap, targets):
    answer = []
    for target in targets:
        res = 0
        for x in target:
            count = 101
            for key in keymap:
                if x in key:
                    count = min(key.index(x)+1, count)
            if count == 101:
                res = -1
                break
            else:
                res += count
        answer.append(res)              
    return answer