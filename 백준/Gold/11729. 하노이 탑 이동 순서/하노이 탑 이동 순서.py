import sys
input = sys.stdin.readline
n = int(input())
answer = []

def hanoi(n,start, end, assist):
    if n==1:
        answer.append([start, end])
        return
    hanoi(n-1, start, assist, end)
    answer.append([start, end])
    hanoi(n-1, assist, end, start)

hanoi(n,1,3,2)
print(len(answer))
for i,j in answer:
    print(i,j)