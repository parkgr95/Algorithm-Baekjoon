# 에라토스테네스의 체
n, k = map(int, input().split())

count = 0
check_list = [True] * (n + 1)
for i in range(2, n + 1):
  for j in range(i, n + 1, i):
    if check_list[j]:
      check_list[j] = False
      count += 1
      if count == k:
        print(j)
        break