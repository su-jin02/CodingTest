# def solution(s):
#     if len(s) == 1:
#         return 1
#     res = 1000

#     def split(n):
#         nonlocal answer
#         arr = ''
#         num = 1
#         for i in range(0,len(s),n):
#             x = s[i:i+n]
#             if arr != x:
#                 if num == 1:
#                     answer += arr
#                 else:
#                     answer += str(num)+arr
#                     num = 1
#                 arr = x
#             else:
#                 num += 1
#         if num != 1:
#             answer += str(num)+arr
#         else:
#             answer += arr

#     for i in range(1,len(s)):
#         answer = ''
#         split(i)
#         if len(answer) < res:
#             res = len(answer)

#     return res
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1): #자를 단위
        tmp, idx = "", 0
        while idx < len(s):
            c, n = s[idx:idx+i], 1
            while c == s[idx+i: idx+i+i]:
                idx, n = idx + i, n + 1
                
            if n != 1:
                tmp += (str(n) + c)
            else:
                tmp += c
            idx += i
        
        if len(tmp) < answer:
            answer = len(tmp) 

    return answer