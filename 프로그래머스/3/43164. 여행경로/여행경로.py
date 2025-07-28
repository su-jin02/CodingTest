from collections import deque
def solution(tickets): 
    n = len(tickets)
    visited = [0] * n
    answer = []
    
    def dfs(visited, num, ans):
        nonlocal answer
        if num == n:
            if answer:
                answer = min(answer, ans)
            else:
                answer = ans[:]
        else:
            for k in range(len(tickets)):
                i, j = tickets[k]
                if visited[k] == 0 and i == ans[-1]:
                    visited[k] = 1
                    dfs(visited, num+1, ans + [j])
                    visited[k] = 0  
    
    for k in range(len(tickets)):
        i, j = tickets[k]
        if i == "ICN":
            visited[k] = 1
            dfs(visited, 1, [i,j])
            visited[k] = 0    
    return answer

