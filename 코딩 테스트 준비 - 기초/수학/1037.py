import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

print(max(a) * min(a))