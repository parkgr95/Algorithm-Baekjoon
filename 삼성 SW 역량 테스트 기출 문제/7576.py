from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(m):
  for j in range(n):
    if graph[i][j] == 1:
      queue.append([i, j])

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
      graph[nx][ny] = graph[x][y] + 1
      queue.append((nx, ny))

result = -2
check = False

for i in graph:
  for j in i:
    if j == 0:
      check = True
    result = max(result, j)

if check:
  print(-1)
if result == 1:
  print(0)
else:
  print(result - 1)