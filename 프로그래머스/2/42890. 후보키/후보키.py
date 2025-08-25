from itertools import combinations
def solution(relation):
    items = [i for i in range(len(relation[0]))]
    answer = 0
    res = set()
    
    for i in range(1,len(relation[0])+1):
        result = combinations(items, i)
        for j in result: #가능한 모든 조합 
            J = frozenset(j)
            #이 조합을 볼지말지 체크
            if any(fk.issubset(J) for fk in res):
                continue
            s = set() 
            for item in relation: #데이터를 보며 후보키 검사
                s.add(tuple(item[k] for k in j) )
            if len(relation) == len(s):
                answer += 1
                res.add(J)
    return answer