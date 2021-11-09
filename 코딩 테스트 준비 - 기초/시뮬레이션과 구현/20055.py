from collections import deque
n, k = map(int, input().split())
arr = deque(map(int, input().split())) # 벨트의 내구도
rob = deque([0] * n)

ans = 1

while True:
  arr.rotate(1)
  rob.rotate(1)
  rob[-1] = 0

  for i in range(-2, -n - 1, -1):
    if rob[i] == 1 and rob[i + 1] == 0 and arr[i + 1 - n] > 0:
        rob[i] = 0
        rob[i + 1] = 1
        arr[i + 1 - n] -= 1
  rob[-1] = 0

  if rob[0] == 0 and arr[0] > 0:
    rob[0] = 1
    arr[0] -= 1
  
  if arr.count(0) >= k:
    break

  ans += 1

print(ans)