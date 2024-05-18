#해결방법 참조
def solution(numbers):
    answer = []
    for i in numbers:
        x = list(bin(i))
        length = len(x)
        for j in range(length-1,1,-1):
            #맨 우측부터 0을 찾음
            if x[j] == '0':
                #해당 값을 1로 변경
                x[j] = '1'
                #이전비트를 0으로 변경
                if j != length-1:
                    x[j+1] = '0'
                break
        #0이 존재하지 않았다면 111 -> 1011
        else:
            x.insert(3,0)
        answer.append(int(''.join(map(str,x)), 2))
    return answer

print(solution([2,7]))
