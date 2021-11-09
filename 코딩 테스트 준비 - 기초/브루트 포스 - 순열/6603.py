import sys
# from itertools import combinations
#
# while True:
#     a = list(map(int, sys.stdin.readline().split()))
#     if a[0] == 0:
#         break
#     del a[0]
#     for c in list(combinations(a, 6)):
#         for x in c:
#             print(x, end='')
#         print()
#     print()

# dfs
def dfs(v, depth):
    if depth == 6:
        for i in range(k):
            if visted[i]:
                print(a[i], end=' ')
        print()
        return

    for i in range(v, k):
        visted[i] = True
        dfs(i+1, depth+1)
        visted[i] = False

visted = [False] * 13

while True:
    a = list(map(int, sys.stdin.readline().split()))
    k = a[0]
    if k == 0:
        break
    a = a[1:]
    dfs(0, 0)
    print()