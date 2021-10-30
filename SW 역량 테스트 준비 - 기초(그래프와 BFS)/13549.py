from collections import deque
import sys
MAX = 100001

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * MAX

q = deque()
q.append(n)
visited[n] = 0
while q:
    now = q.popleft()
    if now == k:
        print(visited[now])
        break
    if 0 <= now*2 < MAX and visited[now*2] == -1:
        q.appendleft(now*2)
        visited[now*2] = visited[now]
    if 0 <= now+1 < MAX and visited[now+1] == -1:
        q.append(now+1)
        visited[now+1] = visited[now] + 1
    if 0 <= now-1 < MAX and visited[now-1] == -1:
        q.append(now-1)
        visited[now-1] = visited[now] + 1