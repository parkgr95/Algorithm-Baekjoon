import sys

def cal(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

for _ in range(int(sys.stdin.readline().rstrip())):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(cal(m, n, x, y))