# 강의섹션7. 알파코드
import sys
input = sys.stdin.readline
x = input()[:-1]
ch= []
res = 0

def DFS(n):
    global res,ch
    if len(n) == 0:
        for i in ch:
            print(i, end='')
        print()
        res += 1
    else:
        for i in range(1,3):
            a = n[0:i]
            b = n[i:]
            if int(a) < 27 and a[0] != '0':
                ch.append(chr(ord('A') + int(a) - 1))
                DFS(b)
                ch.pop()
                if len(b) == 0:
                    break

DFS(x)
print(res)
