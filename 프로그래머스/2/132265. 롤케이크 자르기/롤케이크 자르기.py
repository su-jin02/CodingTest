from collections import Counter
def solution(topping):
    t1 = Counter(topping)
    t2 = set()
    answer = 0
        
    for i in topping:
        t1[i] -= 1
        t2.add(i)
        
        if t1[i] == 0:
            t1.pop(i)
            
        if(len(t1) == len(t2)):
            answer += 1
        elif len(t1) < len(t2):
            break
                
    return answer