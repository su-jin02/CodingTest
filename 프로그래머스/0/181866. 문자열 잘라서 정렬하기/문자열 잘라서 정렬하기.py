def solution(myString):
    answer = []
    x = 0
    
    for i in range(len(myString)):
        if myString[i] == 'x':
            if x != i:  # 빈 문자열이 아니라면 추가
                answer.append(myString[x:i])
            x = i + 1
            
    #마지막 숫자 처리
    if x != len(myString):
        answer.append(myString[x:])
        
    answer.sort()
    return answer