import sys

from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
p = permutations(range(1, n + 1), m)
for i in p:
    print(' '.join(map(str, i)))