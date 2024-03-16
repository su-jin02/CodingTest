#그룹단어체커
import sys
input = sys.stdin.readline
n=int(input())
res = 0
for _ in range(n):
    dic = {}
    word = list(map(str, input().strip()))
    for i in range(len(word)):
        if word[i] in dic:
            if dic[word[i]] != i-1:
                break
            else:
                dic[word[i]] = i
        else:
            dic[word[i]] = i
    else:
        res += 1

print(res)