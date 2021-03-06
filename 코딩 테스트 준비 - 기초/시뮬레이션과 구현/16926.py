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

# deque 이용
from collections import deque
import sys

def rotate_board(r):
    global n, m, B
    q = deque()
    row, col = n, m
    time = min(row, col) // 2
    nx, ny = 0, 0

    while time >= 1:
        for i in range(col-1):
            q.append(B[nx][ny+i])
        for i in range(row-1):
            q.append(B[nx+i][ny+col-1])
        for i in range(col-1):
            q.append(B[nx+row-1][ny+col-1-i])
        for i in range(row-1):
            q.append(B[nx+row-1-i][ny])

        q.rotate(-r)

        for i in range(col-1):
            B[nx][ny+i] = q.popleft()
        for i in range(row-1):
            B[nx+i][ny+col-1] = q.popleft()
        for i in range(col-1):
            B[nx+row-1][ny+col-1-i] = q.popleft()
        for i in range(row-1):
            B[nx+row-1-i][ny] = q.popleft()

        row -= 2
        col -= 2
        nx += 1
        ny += 1
        time = min(row, col) // 2


n, m, r = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rotate_board(r)
for b in B:
    print(*b)