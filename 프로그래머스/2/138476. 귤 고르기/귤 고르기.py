from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    num = 0
    answer = 0
    for x,y in tangerine:
        if num >= k:
            break
        answer += 1
        num += y

    return answer