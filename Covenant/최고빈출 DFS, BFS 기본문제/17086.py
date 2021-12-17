from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not B[nx][ny]:
                B[nx][ny] = B[x][y] + 1
                q.append((nx, ny))

if __name__ == "__main__":
    n, m = map(int, input().split())
    B, q = [], deque()
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(m):
            if temp[j]:
                q.append((i, j))
        B.append(temp)
    bfs()
    ans = 0
    for i in range(n):
        if ans < max(B[i]):
            ans = max(B[i])
    print(ans - 1)