import sys

n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d = (d -1) % 4

ans = 1
turn_time = 0
visited[x][y] = True
while True:
    turn_left()
    nx, ny = x + dx[d], y + dy[d]
    if arr[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        x, y = nx, ny
        turn_time = 0
        ans += 1
    else:
        turn_time += 1
    if turn_time == 4:
        nx, ny = x - dx[d], y - dy[d]
        if arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(ans)