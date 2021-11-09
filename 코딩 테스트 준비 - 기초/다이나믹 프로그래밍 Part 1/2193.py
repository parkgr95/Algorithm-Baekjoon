import sys
input = sys.stdin.readline()
MAX = 91

d = [0] * MAX
d[1] = 1
d[2] = 1
for i in range(3, MAX):
    d[i] = d[i - 1] + d[i - 2]

n = int(input)
print(d[n])