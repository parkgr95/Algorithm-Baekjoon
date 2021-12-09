n, k = map(int, input().split())
B = [int(input()) for _ in range(n)]
d = [0] * (k + 1)
d[0] = 1

for i in B:
    for j in range(1, k + 1):
        if j >= i:
            d[j] += d[j - i]

print(d[k])