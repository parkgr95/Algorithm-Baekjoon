import sys

n = int(sys.stdin.readline().rstrip())

d = [0 for _ in range(31)]
d[2] = 3
for i in range(4, 31, 2):
    d[i] = d[2] * d[i-2]
    for j in range(4, i, 2):
        d[i] += 2 * d[i-j]
    d[i] += 2

sys.stdout.write(str(d[n]))