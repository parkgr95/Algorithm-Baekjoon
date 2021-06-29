import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

p = product(array, repeat=m)
for i in p:
    print(' '.join(map(str, i)))