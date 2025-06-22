from collections import deque

def solution(word):
    answer = 0
    ans = 0
    dic = ['A', 'E', 'I', 'O', 'U']

    def dfs(x):
        nonlocal answer, ans
        if x == word:
            ans = answer
            return
        if len(x) == 5:
            return
        for i in dic:
            answer += 1
            dfs(x + i)

    dfs("")
    return ans
    
    # diction = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    # dq = deque([])
    # prev = 0
    # while "".join(dq) != word:
    #     print(dq)
    #     if len(dq) == 5:
    #         x = dq.pop()
    #         if x == 'U':
    #             while True:
    #                 y = dq.pop()
    #                 if y != 'U':
    #                     prev = diction[y]+1
    #                     dq.append(dic[prev])
    #                     answer += 1
    #                     prev = 0
    #                     break
    #         else:
    #             prev += 1
    #             dq.append(dic[prev])
    #             answer += 1
    #     else:
    #         dq.append(dic[prev])
    #         answer += 1
    # return answer

#자리 가중치
# def solution(word):
#     weight = [781, 156, 31, 6, 1]
#     code   = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

#     idx = 0
#     for i, ch in enumerate(word):
#         idx += code[ch] * weight[i] + 1    # 자리값 기여 + 자기 자신
#     return idx