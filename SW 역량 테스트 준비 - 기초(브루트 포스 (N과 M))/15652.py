import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
p = combinations_with_replacement(range(1, n + 1), m)
for i in p:
    print(' '.join(map(str, i)))