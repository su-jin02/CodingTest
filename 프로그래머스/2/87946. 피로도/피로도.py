from itertools import permutations
def solution(k, dungeons):
    dun = list(permutations(dungeons, len(dungeons)))
    answer = 0
    
    for i in dun:
        cal = k 
        res = 0
        for x,y in i:
            if cal < x:
                break
            else:
                cal -= y
                res += 1
        answer = max(answer, res)
    
    return answer