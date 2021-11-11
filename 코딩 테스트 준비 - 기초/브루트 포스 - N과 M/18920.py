import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(px, py, cnt, total):
    if cnt == k:
        global ans
        ans = max(ans, total)
        return
    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            if visited[x][y]:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]: # 인근에 방문했다면 종료
                    break
            else:
                visited[x][y] = 1
                dfs(x, y, cnt+1, total+arr[x][y])
                visited[x][y] = 0


if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    ans = -1000000
    dfs(0, 0, 0, 0)
    print(ans)
