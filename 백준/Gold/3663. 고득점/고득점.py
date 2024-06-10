import sys
input = sys.stdin.readline
n = int(input())

def solution(name):
    len_name = len(name)
    answer = 0
    rem = 0
    cnt = 1e9
    for i in range(len_name):
        if (name[i] != 'A'):
            cal = ord(name[i])
            answer += min(91-cal, cal-65)

            if i == 0:
                continue
            tmp = rem + len_name - i
            cnt = min(cnt, min(tmp+rem, tmp+len_name-i))
            # 우측이동 후 좌측으로 이동, 좌측이동 후 우측 이동인지
            rem = i
    cnt = min(rem, cnt) #다 훑기 vs 특정 숫자만
    return answer + cnt

for i in range(n):
    x = input().strip()
    print(solution(x))
