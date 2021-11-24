import sys

n, m, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        value = arr[x][y]

        for j in range(i + 1, n - i):  # 좌
            x = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp

        for j in range(i + 1, m - i):  # 하
            y = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp

        for j in range(i + 1, n - i):  # 우
            x = n - j - 1
            temp = arr[x][y]
            arr[x][y] = value
            value = temp

        for j in range(i + 1, m - i):  # 상
            y = m - j - 1
            temp = arr[x][y]
            arr[x][y] = value
            value = temp

for a in arr:
    print(*a)