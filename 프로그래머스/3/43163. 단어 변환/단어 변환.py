def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = len(words)

    def dfs(word, find):
        nonlocal answer, words
        for i in range(len(words)):
            if find[i] == 0:
                diff = 0
                #단어가 다른개 1개인지 판단
                for j in range(len(word)):
                    if diff > 1:
                        break
                    if word[j] != words[i][j]:
                        diff += 1
                #맞다면 탐색
                if diff == 1:
                    if words[i] == target:
                        temp = 0
                        for i in find:
                            if i == 1:
                                temp += 1
                        answer = min(answer, temp+1)
                    else:
                        find[i] = 1
                        dfs(words[i], find)
                        find[i] = 0

    dfs(begin, [0] * len(words))
    return answer
        
        
