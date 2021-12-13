from collections import deque

def bfs(start):
    q = deque([start])
    while q:
        x = q.popleft()
        if x == k:
            time[k] = time[x]
            return
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < MAX and not time[nx]:
                if nx == 2 * x and x != 0:
                    time[nx] = time[x]
                    q.appendleft(nx)
                else:
                    time[nx] = time[x] + 1
                    q.append(nx)

MAX = 1000001
n, k = map(int, input().split())
time = [0] * MAX
bfs(n)
print(time[k])

# 회고: x가 0일때를 고려하지 않았다. 또한 순간이동을 최대한 하는 방향으로 고려하지 않았다. 순간이동을 많이 하는 방향으로 고려하면 굳이 값을 비교하지 않아도 된다.