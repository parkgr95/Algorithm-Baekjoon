'''
date : 0415
idea : 구현
'''
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def destroy(i, left):
    i, j = r - i, 0
    if left == 1:
        for k in range(c):
            if cave[i][k] == 'x':
                cave[i][k] = '.'
                j = k
                break
    else:
        for k in range(c - 1, -1, -1):
            if cave[i][k] == 'x':
                cave[i][k] = '.'
                j = k
                break

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < r and 0 <= nj < c:
            if cave[ni][nj] == 'x':
                dq.append((ni, nj))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * c for _ in range(r)]
    visited[x][y] = 1
    fall_list = []
    while q:
        x, y = q.popleft()
        if x == r - 1:
            return
        if cave[x + 1][y] == '.':
            fall_list.append([x, y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and cave[nx][ny] == 'x' and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])

    fall(visited, fall_list)


def fall(visited, fall_list):
    k, flag = 1, 0
    while True:
        for i, j in fall_list:
            if i + k == r - 1:  # 떨어지는 곳이 바닦일경우 
                flag = 1
                break
            if cave[i + k + 1][j] == 'x' and not visited[i + k + 1][j]:  # 떨어지는 곳이 다른 미네랄이 있다면 
                flag = 1
                break
        if flag:
            break
        k += 1

    for i in range(r - 2, -1, -1):
        for j in range(c):
            if cave[i][j] == 'x' and visited[i][j]:
                cave[i][j] = '.'
                cave[i + k][j] = 'x'


r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]
n = int(input())
sticks = list(map(int, input().split()))
dq = deque()

left = 1
while n:
    index = sticks.pop(0)
    destroy(index, left)

    while dq:
        x, y = dq.popleft()
        bfs(x, y)

    left *= -1
    n -= 1

for i in range(r):
    for j in range(c):
        print(cave[i][j], end='')
    print()