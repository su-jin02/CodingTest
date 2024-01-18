# 강의섹션7. 동전바꿔주기
import sys
input = sys.stdin.readline
t = int(input())
k = int(input())
ch1 = []
ch2 = []
for _ in range(k):
    a, b = map(int, input().split())
    ch1.append(a)
    ch2.append(b)
res = 0

def DFS(n, total):
    global res
    if total > t:
        return
    if total == t:  # 추가(원하는 가격이 나오면 밑에 레벨 탐색 X)
        res += 1
        return

    if n == k:
        if total == t:
            res += 1
        return
    else:
        for i in range(ch2[n] + 1):
            DFS(n + 1, total + ch1[n] * i)


DFS(0, 0)
print(res)