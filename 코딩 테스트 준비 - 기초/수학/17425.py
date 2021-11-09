import sys

MAX = 1000001
d = [0] * MAX

for i in range(1, MAX):
    for j in range(i, MAX, i):
        d[j] += i
    d[i] += d[i-1]

for _ in range(int(sys.stdin.readline().rstrip())):
    print(d[int(sys.stdin.readline().rstrip())])