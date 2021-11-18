import sys

n = int(sys.stdin.readline().rstrip())

mod = 9901
no, left, right = 1, 0, 0

for i in range(n):  # no = no + left + right, left = no + right, no + left
    no = no + left + right
    left, right = no - left, no - right

sys.stdout.write(str((no + left + right) % mod))