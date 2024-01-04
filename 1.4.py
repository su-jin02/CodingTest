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

#한줄평 : dfs문제로 풀고 싶어 도전하였으나 거의 그냥 for문과 다를바가 없이 구현해버렸고 런타임 에러를 마주하고 알고리즘을 사용하지 않고 풀었다..
#좀 더 실력을 키워서 dfs방식으로 다시 풀어봐야겠다.
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