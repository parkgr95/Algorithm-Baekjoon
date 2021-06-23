def dec(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input())
array = list(map(int, input().split()))

answer = 0
for arr in array:
    if dec(arr):
        answer += 1
print(answer)