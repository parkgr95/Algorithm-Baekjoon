import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

visited = [False] * n
answer = []

def dfs(depth):
    if depth == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(n):
        if not visited[i]:
            answer.append(array[i])
            dfs(depth + 1)
            answer.pop()
dfs(0)