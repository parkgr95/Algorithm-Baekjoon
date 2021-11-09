import sys

m = int(sys.stdin.readline())

s = set()
for _ in range(m):
    x = sys.stdin.readline().split()
    if len(x) == 1:
        if x[0] == "all":
            s = set([i for i in range(1, 21)])
            print(s)
        else:
            s = set()
        continue

    a, b = x[0], int(x[1])
    if a == "add":
        s.add(b)
    if a == "remove":
        s.discard(b)
    if a == "check":
        print(1 if int(b) in s else 0)
    if a == "toggle":
        s.discard(b) if b in s else s.add(b)