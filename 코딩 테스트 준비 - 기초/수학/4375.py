import sys

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        ans = '1'
        while True:
            if int(ans) % n == 0:
                print(len(ans))
                break
            ans += '1'
    except EOFError:
        break
