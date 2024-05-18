from collections import Counter
def solution(want, number, discount):
    answer = 0
    num = 0
    while len(discount) - num - 9 > 0:
        count = Counter(discount[num:num+10])
        for i in range(len(want)):
            if want[i] in count:
                if count[want[i]] != number[i]:
                    break
            else:
                break
        else:
            answer += 1
        num += 1
    return answer