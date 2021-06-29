import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

p = permutations(array, m)
for i in p:
    print(' '.join(map(str, i)))