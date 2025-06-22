from collections import deque
def solution(n, computers):
    q = deque()
    find = [[0] * n for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if find[i][j] == 0:
                if computers[i][j] == 1:
                    q.append(j)
                find[i][j] = 1
                find[j][i] = 1
        if q:
            answer += 1
            while q:
                x = q.popleft()
                for k in range(n):
                    if find[x][k]==0:
                        if computers[x][k]==1:
                            q.append(k)
                        find[x][k] = 1
                        find[k][x] = 1

    return answer