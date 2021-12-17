s = str(input())
bomb = str(input())
stack = []
for c in s:
    stack.append(c)
    if stack[-1] == bomb[-1] and "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    print("".join(stack))
else:
    print("FRULA")