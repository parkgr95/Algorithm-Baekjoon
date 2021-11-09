import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    ans = 0
    for i in range(1, n+1):
        ans += (n // i) * i
    print(ans)