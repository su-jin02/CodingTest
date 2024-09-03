from itertools import permutations
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
per = list(permutations(arr, m))
unique_permutations = sorted(set(per))

for perm in unique_permutations:
    print(' '.join(map(str, perm)))