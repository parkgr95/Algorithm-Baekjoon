# dfs
def dfs(x, y, direction):
    global count
    if x == n - 1 and y == n - 1:
        count += 1
    if direction == 0:  # 가로
        if y < n - 1 and B[x][y + 1] == 0:
            dfs(x, y + 1, 0)
        if x < n - 1 and y < n - 1 and B[x][y + 1] == 0 and B[x + 1][y + 1] == 0 and B[x + 1][y] == 0:
            dfs(x + 1, y + 1, 2)
    elif direction == 1:  # 세로
        if x < n - 1 and B[x + 1][y] == 0:
            dfs(x + 1, y, 1)
        if x < n - 1 and y < n - 1 and B[x][y + 1] == 0 and B[x + 1][y + 1] == 0 and B[x + 1][y] == 0:
            dfs(x + 1, y + 1, 2)
    else:  # 대각선
        if y < n - 1 and B[x][y + 1] == 0:
            dfs(x, y + 1, 0)
        if x < n - 1 and B[x + 1][y] == 0:
            dfs(x + 1, y, 1)
        if x < n - 1 and y < n - 1 and B[x][y + 1] == 0 and B[x + 1][y + 1] == 0 and B[x + 1][y] == 0:
            dfs(x + 1, y + 1, 2)

n = int(input())
B = [list(map(int, input().split())) for i in range(n)]
count = 0
dfs(0, 1, 0)
print(count)