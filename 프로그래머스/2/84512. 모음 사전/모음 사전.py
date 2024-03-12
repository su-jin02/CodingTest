def solution(word):
    from itertools import product
    words = []
    answer = {}
    for i in range(5):
        for x in list(product("AEIOU", repeat=i+1)):
            words.append(''.join(x))
    words.sort()
    for i, x in enumerate(words):
        answer[x] = i + 1
    
    return answer[word]

    

    
    
    
    