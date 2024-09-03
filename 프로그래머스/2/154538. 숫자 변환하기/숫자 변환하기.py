from collections import deque
def solution(x, y, n):
    def bfs(x):
        q = deque()
        dist[x] = 1
        q.append(x)

        while q:
            x = q.popleft()
            if x * 3 <= y and dist[x * 3] == 0:
                dist[x * 3] = dist[x] + 1
                q.append(x * 3)
            if x * 2 <= y and dist[x * 2] == 0:
                dist[x * 2] = dist[x] + 1
                q.append(x * 2)
            if x + n <= y and dist[x + n] == 0:
                dist[x + n] = dist[x] + 1
                q.append(x + n)

    dist = [0] * 1000001
    bfs(x)

    return dist[y]-1
