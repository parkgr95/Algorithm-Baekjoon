import sys

n, m = map(int, sys.stdin.readline().split())

visited = [False] * n
answer = []

def dfs(depth):
    if depth == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(i + 1)
            dfs(depth + 1)
            visited[i] = False
            answer.pop()

dfs(0)