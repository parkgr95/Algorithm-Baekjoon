'''
date : 0414
idea : 구현
'''
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while swan_q:
        x, y = swan_q.popleft()
        if x == x2 and y == y2:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not swan_visited[nx][ny]:
                if B[nx][ny] == '.':
                    swan_q.append((nx, ny))
                else:
                    nxt_sq.append((nx, ny))
                swan_visited[nx][ny] = 1
    return False

def melt():
    while ice_q:
        x, y = ice_q.popleft()
        if B[x][y] == 'X':
            B[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not ice_visited[nx][ny]:
                if B[nx][ny] == '.':
                    ice_q.append((nx, ny))
                else:
                    nxt_iq.append((nx, ny))
                ice_visited[nx][ny] = 1

if __name__ == '__main__':
    r, c = map(int, input().split())
    swan_visited = [[0] * c for _ in range(r)]
    ice_visited = [[0] * c for _ in range(r)]

    B, swan = [], []
    swan_q, nxt_sq, ice_q, nxt_iq = deque(), deque(), deque(), deque()

    for i in range(r):
        arr = list(input())
        B.append(arr)
        for j in range(c):
            if arr[j] == 'L':
                swan.extend((i, j))
                ice_q.append((i, j))
            elif arr[j] == '.':
                ice_visited[i][j] = 1
                ice_q.append((i, j))

    x1, y1, x2, y2 = swan
    swan_q.append((x1, y1))
    B[x1][y1], B[x2][y2], swan_visited[x1][y1] = '.', '.', 1
    cnt = 0

    while True:
        melt()
        if bfs():
            print(cnt)
            break
        swan_q, ice_q = nxt_sq, nxt_iq
        nxt_sq, nxt_iq = deque(), deque()
        cnt += 1
