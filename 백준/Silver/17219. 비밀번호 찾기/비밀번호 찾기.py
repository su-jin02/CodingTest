import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for _ in range(n):
    site, password = map(str, input().split())
    dic[site] = password

for _ in range(m):
    site = input().strip()
    print(dic[site])