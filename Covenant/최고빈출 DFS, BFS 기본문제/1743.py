from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    B[i][j] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and B[nx][ny]:
                q.append((nx, ny))
                B[nx][ny] = 0
                cnt += 1
    return cnt

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    B = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        B[i-1][j-1] = 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if B[i][j]:
                ans = max(ans, bfs(i, j))
    print(ans)