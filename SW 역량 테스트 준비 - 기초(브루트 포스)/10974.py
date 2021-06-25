import sys

def next_permutation(array):
    j = 0
    check = False
    for i in range(n - 1, 0, -1):
        if array[i - 1] < array[i]:
            j = i - 1
            break
    for i in range(n - 1, 0, -1):
        if array[j] < array[i]:
            array[j], array[i] = array[i], array[j]
            array = array[:j + 1] + sorted(array[j + 1:])
            check = True
            break
    if check:
        return array
    if not check:
        return -1

n = int(sys.stdin.readline())
array = [i + 1 for i in range(n)]

for i in array:
    print(i, end=' ')

if len(array) != 1:
    print()
    answer = array
    while True:
        answer = next_permutation(answer)
        if answer == -1:
            break
        for i in answer:
            print(i, end=' ')
        print()
