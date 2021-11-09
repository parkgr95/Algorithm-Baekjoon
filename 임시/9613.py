from itertools import combinations

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

t = int(input())
for _ in range(t):
  data = list(map(int, input().split()))
  data = data[1:]
  answer = 0
  for a, b in list(combinations(data, 2)):
    answer += gcd(a, b)
  print(answer)