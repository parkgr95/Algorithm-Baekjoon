from collections import deque

n = int(input())
visited = [[-1] * (n + 1) for _ in range(n + 1)]
visited[1][0] = 0
q = deque()
q.append((1, 0))  # 이모티콘의 개수, 클립보드의 개수
while q:
    s, c = q.popleft()
    if visited[s][s] == -1:  # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        visited[s][s] = visited[s][c] + 1
        q.append((s, s))
    if s + c <= n and visited[s + c][c] == -1:  # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        visited[s + c][c] = visited[s][c] + 1
        q.append((s + c, c))
    if s - 1 >= 0 and visited[s - 1][c] == -1:  # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        visited[s - 1][c] = visited[s][c] + 1
        q.append((s - 1, c))
answer = -1
for i in range(n + 1):
    if visited[n][i] != -1 and (answer == -1 or visited[n][i] < answer):
        answer = visited[n][i]
print(answer)

# 회고: 최단시간은 bfs