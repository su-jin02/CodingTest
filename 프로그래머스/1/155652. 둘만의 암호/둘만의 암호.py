def solution(s, skip, index):
    answer = ''
    for i in s:
        j = 1
        num = index
        while True:
            if j > num:
                break
            x = chr((ord(i) + j - 97) % 26 + 97)  
            if x in skip:
                num += 1
            j += 1
        answer += x  
    return answer