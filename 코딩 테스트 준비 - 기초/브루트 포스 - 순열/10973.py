import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

check = False

j = 0
for i in range(n - 1, 0, -1):
    if array[i - 1] > array[i]:
        j = i - 1
        break
for i in range(n - 1, 0, -1):
  if array[j] > array[i]:
      array[j], array[i] = array[i], array[j]
      array = array[:j + 1] + sorted(array[j + 1:], reverse=True)
      check = True
      break
if check:
    for i in array:
        print(i, end=' ')
if not check:
    print(-1)