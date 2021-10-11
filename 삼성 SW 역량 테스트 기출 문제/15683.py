from collections import deque
import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(cnt):
    global check, ans
    if cnt == cctv_n:
        tmp = 0
        for i in range(n):
            for j in range(m):
                if not B[i][j] and not check[i][j]:
                    tmp += 1
        return tmp

    x, y = cctv[cnt][0], cctv[cnt][1]
    for k in range(4):
        new_dir = []
        if B[x][y] == 1:
            new_dir.append(k)
        elif B[x][y] == 2:
            new_dir.append(k)
            new_dir.append((k + 2) % 4)
        elif B[x][y] == 3:
            new_dir.append(k)
            new_dir.append((k - 1) % 4)
        elif B[x][y] == 4:
            new_dir.append(k)
            new_dir.append((k - 1) % 4)
            new_dir.append((k + 2) % 4)
        elif B[x][y] == 5:
            new_dir.append(k)
            new_dir.append((k - 1) % 4)
            new_dir.append((k + 1) % 4)
            new_dir.append((k + 2) % 4)
        q = deque()
        for d in new_dir:
            nx, ny = x + dx[d], y + dy[d]
            while 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny] and B[nx][ny] != 6:
                    check[nx][ny] = True
                    q.append((nx, ny))
                elif B[nx][ny] == 6: break
                nx += dx[d]
                ny += dy[d]
        ans = min(ans, solution(cnt + 1))
        while q:
            qx, qy = q.popleft()
            if not B[qx][qy]:
                check[qx][qy] = False
        if B[x][y] == 5:
            break
    return ans

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    cctv = []
    cctv_n = 0
    ans = 0
    check = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if B[i][j] and B[i][j] != 6:
                cctv.append((i, j))
                check[i][j] = True
                cctv_n += 1
            if not B[i][j]:
                ans += 1
    solution(0)
    print(ans)
