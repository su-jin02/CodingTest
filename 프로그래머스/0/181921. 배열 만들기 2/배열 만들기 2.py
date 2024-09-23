def solution(l, r):
    answer = []
    num_list = [num for num in range(l,r+1)]
    a = ["0", "5"]
    for num in num_list:
        Bol = True
        str_num = str(num)
        for k in str_num:
            if k not in a:
                Bol = False
                break
        if Bol == True:
            answer.append(num)
    if answer == []:
        return [-1]
    return answer