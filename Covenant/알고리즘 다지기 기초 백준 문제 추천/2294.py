n, k = map(int, input().split())
B = [int(input()) for _ in range(n)]
d = [0] * (k + 1)

for i in range(1, k + 1):
    temp = []
    for j in B:
        if i >= j and d[i - j] != -1:
            temp.append(d[i - j])
    if not temp:
        d[i] = -1
    else:
        d[i] = min(temp) + 1

print(d[k])