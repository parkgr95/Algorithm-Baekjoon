from itertools import combinations
import sys

l, c = map(int, sys.stdin.readline().split())
arr = sorted(list(map(str, sys.stdin.readline().split())))

for c in combinations(arr, l):
    cnt = 0
    for letter in c:
        if letter in "aeiou":
            cnt += 1

    if 1 <= cnt <= (l-2):
        print(''.join(c))