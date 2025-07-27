import heapq
def solution(n, k, enemy):
    h = []
    for i in range(len(enemy)):
        if n < enemy[i]:
            if k > 0:
                if h:
                    #이전까지 공격 중 최대를 막을지? 지금을 막을지?
                    if -h[0] > enemy[i]:
                        n += -(heapq.heappop(h))
                        heapq.heappush(h, -enemy[i])  
                        n -= enemy[i]
                k -= 1
            else:
                return i
        else:
            heapq.heappush(h, -enemy[i])  
            n -= enemy[i]
    else:
        return len(enemy)