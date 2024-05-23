def solution(s):
    if len(s) == 1:
        return 1
    res = 1000

    def split(n):
        nonlocal answer
        arr = ''
        num = 1
        for i in range(0,len(s),n):
            x = s[i:i+n]
            if arr != x:
                if num == 1:
                    answer += arr
                else:
                    answer += str(num)+arr
                    num = 1
                arr = x
            else:
                num += 1
        if num != 1:
            answer += str(num)+arr
        else:
            answer += arr

    for i in range(1,len(s)):
        answer = ''
        split(i)
        if len(answer) < res:
            res = len(answer)

    return res