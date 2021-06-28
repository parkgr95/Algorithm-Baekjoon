import sys

from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
c = combinations(range(1, n + 1), m)
for i in c:
    print(' '.join(map(str, i)))