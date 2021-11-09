import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

answer = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j) == True:
            answer.append(count)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
