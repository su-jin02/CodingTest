import sys
from collections import Counter
input = sys.stdin.readline
x = input().strip().upper()
counter = Counter(x).most_common()
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print('?')
else:
    print(counter[0][0])