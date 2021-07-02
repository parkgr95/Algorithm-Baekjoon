n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

min_, max_ = 1e9, -1e9

def dfs(i, answer, add, sub, mul, div):
  global max_, min_
  if i == n:
      max_ = max(answer, max_)
      min_ = min(answer, min_)
      return

  else:
      if add:
          dfs(i+1, answer+arr[i], add-1, sub, mul, div)
      if sub:
          dfs(i+1, answer-arr[i], add, sub-1, mul, div)
      if mul:
          dfs(i+1, answer*arr[i], add, sub, mul-1, div)
      if div:
          dfs(i+1, int(answer/arr[i]), add, sub, mul, div-1)

dfs(1, arr[0], add, sub, mul, div)
print(max_)
print(min_)