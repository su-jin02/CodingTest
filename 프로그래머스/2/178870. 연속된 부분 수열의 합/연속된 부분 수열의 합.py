def solution(sequence, k):
    num = 0
    for i in range(len(sequence)-1, -1, -1):
        num += sequence[i]
        if num > k:
            num -= sequence.pop() 
        if num == k: #중복 처리
            while sequence[i-1] == sequence[-1] and i>0:
                i-=1
                sequence.pop()

            return [i, len(sequence)-1]
