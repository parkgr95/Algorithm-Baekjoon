import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
p = product(range(1, n + 1), repeat=m)
for i in p:
    print(' '.join(map(str, i)))