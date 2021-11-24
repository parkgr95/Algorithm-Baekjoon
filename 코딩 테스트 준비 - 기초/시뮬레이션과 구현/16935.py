import sys

def calc_1():
    global arr
    arr = arr[::-1]

def calc_2():
    global arr
    for i in range(n):
        arr[i] = arr[i][::-1]

def calc_3():
    global arr, n, m
    n, m = m, n
    new_arr = [list(row)[::-1] for row in zip(*arr)]
    arr = new_arr

def calc_4():
    global arr, n, m
    n, m = m, n
    new_arr = [list(row) for row in list(zip(*arr))[::-1]]
    arr = new_arr

def calc_5():
    global arr
    new_arr = [[0] * m for _ in range(n)]
    halfn = n // 2
    halfm = m // 2

    for i in range(halfn):
        for j in range(halfm):
            new_arr[i][j + halfm] = arr[i][j]
    for i in range(halfn):
        for j in range(halfm, m):
            new_arr[i + halfn][j] = arr[i][j]
    for i in range(halfn, n):
        for j in range(halfm, m):
            new_arr[i][j - halfm] = arr[i][j]
    for i in range(halfn, n):
        for j in range(halfm):
            new_arr[i - halfn][j] = arr[i][j]
    arr = new_arr

def calc_6():
    global arr
    new_arr = [[0] * m for _ in range(n)]
    halfn = n // 2
    halfm = m // 2

    for i in range(halfn):
        for j in range(halfm):
            new_arr[i + halfn][j] = arr[i][j]
    for i in range(halfn, n):
        for j in range(halfm):
            new_arr[i][j + halfm] = arr[i][j]
    for i in range(halfn, n):
        for j in range(halfm, m):
            new_arr[i - halfn][j] = arr[i][j]
    for i in range(halfn):
        for j in range(halfm, m):
            new_arr[i][j - halfm] = arr[i][j]
    arr = new_arr

if __name__ == '__main__':
    n, m, r = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    for op in list(map(int, sys.stdin.readline().split())):
        if op == 1:
            calc_1()
        elif op == 2:
            calc_2()
        elif op == 3:
            calc_3()
        elif op == 4:
            calc_4()
        elif op == 5:
            calc_5()
        elif op == 6:
            calc_6()

    for a in arr:
        print(*a)