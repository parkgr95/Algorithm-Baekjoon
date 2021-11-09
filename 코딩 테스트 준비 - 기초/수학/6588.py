import sys

check_list = [True] * int(1e6)

for i in range(2, len(check_list)):
    for j in range(2 * i, len(check_list), i):
        if check_list[j]:
            check_list[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(3, n):
        if check_list[i] and check_list[n - i]:
            print("%d = %d + %d" % (n, i, n - i))
            break

    else:
        print("Goldbach's conjecture is wrong.")