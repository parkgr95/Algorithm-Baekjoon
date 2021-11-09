import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x - 1, y + 1)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
        return True
    return False

while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w, h) == (0, 0):
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                answer += 1
    print(answer)
