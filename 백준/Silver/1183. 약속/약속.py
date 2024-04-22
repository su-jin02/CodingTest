#풀이 참고
#a-b시간을 정렬하여 중간값만큼 약속시간을 이동하여 기다리는 시간의 합이 최소가 되도록 함
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    a, b = map(int, input().split())
    numbers.append(b - a)

numbers = sorted(numbers)

res = 0
if len(numbers) % 2 == 0:
    start = len(numbers) // 2 - 1
    res = numbers[start + 1] - numbers[start] + 1
else:
    res = 1

print(res)

