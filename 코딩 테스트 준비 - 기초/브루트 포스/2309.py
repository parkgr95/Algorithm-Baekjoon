import sys
from itertools import combinations

array = []
for _ in range(9):
  array.append(int(sys.stdin.readline()))
array.sort()

for answer in list(combinations(array, 7)):
  if sum(answer) == 100:
    for i in range(7):
      print(answer[i])
    break