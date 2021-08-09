import sys

if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline().rstrip())):
        n = int(sys.stdin.readline().rstrip())

        array = [[0]*100000, [0]*100000]
        for idx, var in enumerate(map(int, sys.stdin.readline().split())):
            array[0][idx] = var
        for idx, var in enumerate(map(int, sys.stdin.readline().split())):
            array[1][idx] = var

        array[0][1] += array[1][0]
        array[1][1] += array[0][0]
        for i in range(2, n):
            array[0][i] += max(array[1][i - 1], array[1][i - 2])
            array[1][i] += max(array[0][i - 1], array[0][i - 2])

        print(max(array[0][n - 1], array[1][n - 1]))