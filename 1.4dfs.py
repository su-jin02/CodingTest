#백준1388
import sys

def width(col, row):  #가로 검사
    global result
    if row == b:
        return
    if ch[col][row] == '-':
        ch[col][row] = 0
        width(col, row+1)

def length(col, row): #세로 검사
    global result
    if col == a:
        return
    if (ch[col][row] == '|'):
        ch[col][row] = 0
        length(col+1, row)

a,b = map(int,sys.stdin.readline().split())
ch = list(list(sys.stdin.readline().strip()) for _ in range(a))
result = 0
for i in range(a):
    for j in range(b):
        if(ch[i][j] == '-'):
            width(i,j+1)
            result += 1
        elif (ch[i][j] == '|'):
            length(i+1,j)
            result += 1

print(result)

