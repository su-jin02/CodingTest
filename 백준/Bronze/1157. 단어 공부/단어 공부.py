import sys
from collections import Counter
input = sys.stdin.readline
x = input().strip().upper()
a=[]
for i in range(65,91):
    a.append(x.count(chr(i)))
if a.count(max(a)) > 1:
    print("?")
else: print(chr(a.index(max(a))+65))

#수정전
# counter = Counter(x).most_common()
# if len(counter) > 1 and counter[0][1] == counter[1][1]:
#     print('?')
# else:
#     print(counter[0][0])
