import sys
from itertools import permutations

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

answer = 0
array = permutations(data)
for arr in array:
    max_ = 0
    for i in range(n - 1):
        max_ += abs(arr[i] - arr[i + 1])
    answer = max(answer, max_)
print(answer)
