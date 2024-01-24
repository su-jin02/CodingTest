#백준1388
import sys
a,b = map(int,sys.stdin.readline().split())
lst = list(list(sys.stdin.readline().strip()) for _ in range(a))
result = 0
ch=[0,0]

for i in range(a):
    for j in range(b):
        if(lst[i][j] == '-'):
            ch[0] = 1
        else:
            if(ch[0] == 1):
                result +=1
            ch[0] = 0
    if (ch[0] == 1):
        result += 1
    ch[0] = 0

for i in range(b):
    for j in range(a):
        if(lst[j][i] == '|'):
            ch[1] = 1
        else:
            if(ch[1] == 1):
                result +=1
            ch[1] = 0
    if (ch[1] == 1):
        result += 1
    ch[1] = 0

print(result)

#한줄평 : dfs문제로 풀고 싶었으나 그냥 for문만 이용해서 품.
#더 나은 코드
import sys
a,b = map(int,sys.stdin.readline().split())
lst = list(list(sys.stdin.readline().strip()) for _ in range(a))
result = 0

for i in range(a):
    x=''
    for j in range(b):
        if(lst[i][j] == '-'): #처음 -가 등장시 카운트
            if(lst[i][j] != x):
                result += 1
        x = lst[i][j]

for i in range(b):
    x = ''
    for j in range(a):
        if(lst[j][i] == '|'):
            if (lst[j][i] == x):
                result+=1
        x=lst[j][i]

print(result)