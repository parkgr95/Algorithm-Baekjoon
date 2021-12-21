n = int(input())
t, p = [], []
d = [0] * (n + 1)
MAX = 0
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
for i in range(n - 1, -1, -1):
    time = t[i] + i
    if time <= n:
        d[i] = max(p[i] + d[time], MAX)
        MAX = d[i]
    else:
        d[i] = MAX
print(MAX)