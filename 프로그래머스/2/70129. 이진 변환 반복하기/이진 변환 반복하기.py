def solution(s):
    answer = [0, 0]
    def helper(s):
        count0 = 0
        count1 = 0
        if s == '1':
            return
        else:
            for i in s:
                if i == '0':
                    count0 += 1
                else:
                    count1 += 1

            answer[0] += 1
            answer[1] += count0
            helper(binary(count1))

    helper(s)
    return answer

def binary(n):
    res = []
    while n>0:
        res.insert(0,n%2)
        n = n//2
    return ''.join(map(str, res))