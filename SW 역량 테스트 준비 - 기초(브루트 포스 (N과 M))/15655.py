import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

c = combinations(array, m)
for i in c:
    print(' '.join(map(str, i)))