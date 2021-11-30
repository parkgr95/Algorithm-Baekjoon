from collections import deque
import sys

def rotate(r):
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
rotate(r)
for b in B:
    print(*b)