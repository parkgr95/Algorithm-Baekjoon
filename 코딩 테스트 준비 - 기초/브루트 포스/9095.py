import sys
t = int(sys.stdin.readline())

array = [1, 2, 4]
for i in range(3, 10):
    array.append(array[i - 1] + array[i - 2] + array[i - 3])
for _ in range(t):
    n = int(sys.stdin.readline())
    print(array[n - 1])