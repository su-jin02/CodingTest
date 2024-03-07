n = int(input())
result = 0

student = [list(input().split()) for _ in range(n)]

student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(student[i][0])