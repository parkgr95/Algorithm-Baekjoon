# 완전 탐색
import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(1, n + 1):
    for combination in combinations(array, i):
        if sum(combination) == s:
            answer += 1

print(answer)

# # dfs
# import sys
#
# def dfs(index, sum):
#     global count
#     if index >= n:
#         return
#     sum += array[index]
#     if sum == s:
#         count += 1
#     dfs(index + 1, sum - array[index])
#     dfs(index + 1, sum)
#
# n, s = map(int, sys.stdin.readline().split())
# array = list(map(int, sys.stdin.readline().split()))
# count = 0
# dfs(0, 0)
# print(count)