import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

c = combinations_with_replacement(array, m)
for i in c:
    print(' '.join(map(str, i)))