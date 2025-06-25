import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    while scoville and scoville[0] < K:
        first = heapq.heappop(scoville)   # 최소
        if not scoville:                  # 재료가 부족하면 실패
            return -1
        second = heapq.heappop(scoville)  # 두 번째 최소
        new = first + second * 2
        heapq.heappush(scoville, new) 
        answer += 1
    return answer