def solution(citations):
    citations.sort(reverse=True)  # 인용 수를 내림차순 정렬
    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i
        
    return len(citations)