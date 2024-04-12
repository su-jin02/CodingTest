def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        res = 0
        for target in targets[i]:
            count = 101
            for key in keymap:
                if target in key:
                    count = min(key.index(target)+1, count)
            if count == 101:
                res = -1
                break
            else:
                res += count
        answer.append(res)
                    
    return answer