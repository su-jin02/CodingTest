def solution(n, wires):
    answer = 100
    wire = [[] for _ in range(n + 1)]
    for x, y in wires:
        wire[x].append(y)
        wire[y].append(x)

    def find(n,x):
        if len(wire[n]) == 0:
            return
        else:
            for i in wire[n]:
                if visited[i] == 0:
                    visited[n] = 1
                    res[x] += 1
                    find(i,x)
            return

        # 선 하나씩 없애기
    for x, y in wires:
        visited = [0] * (n + 1)
        visited[x] = 1
        visited[y] = 1
        res = [0,0]
        find(x,0)
        find(y,1)
        answer = min(answer, abs(res[0]-res[1]))
    return answer