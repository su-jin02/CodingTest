#입력값에 가장 가까운 무게 선택하기
import sys

def DFS(level, sum):
    global result

    if sum > a:
        result = max(result, sum - lst[level - 1])
        return

    if level == b:
        result = max(result, sum)
    else:
        DFS(level+1, sum+lst[level])
        DFS(level+1, sum)


a,b = map(int,sys.stdin.readline().split())
lst = list(int(sys.stdin.readline()) for _ in range(b))
result = 0
DFS(0,0)
print(result)

# --------------------------
# => 위와 같은 방식으로 해결시 타임초과 발생
# 해설풀이
# 밑에 가지들을 다 더해도 최대 값을 넘지 못한다면 더 탐색할 필요가 없음
# --------------------------

def DFS(level, sum, now):
    global result

    if(sum + total-now < result): #탐색을 계속할만한지 체크
        return

    if sum > a: #이미 목표값을 초과했는지 체크
        result = max(result, sum - lst[level - 1])
        return

    if level == b: #마지막 레벨에 도달했는지 체크
        result = max(result, sum)
    else:
        DFS(level+1, sum+lst[level], now+lst[level])
        DFS(level+1, sum, now+lst[level])


a,b = map(int,sys.stdin.readline().split())
lst = list(int(sys.stdin.readline()) for _ in range(b))
total = sum(lst)
result = 0
DFS(0,0,0)
print(result)