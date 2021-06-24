import sys

e, s, m = map(int, sys.stdin.readline().split())

answer = 1
while True:
    if (answer - e) % 15 == 0 and (answer - s) % 28 == 0 and (answer - m) % 19 == 0:
        print(answer)
        break
    answer += 1