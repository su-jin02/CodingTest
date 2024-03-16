import sys
input = sys.stdin.readline
res = 0
n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
a.sort(reverse=True)

sort_b = sorted(b)
rank = []
for i in sort_b:
    rank.append(b.index(i))

for i in range(n):
    res += a[i]*b[rank[i]]

print(res)