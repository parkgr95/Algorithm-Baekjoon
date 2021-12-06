s = input()
stack = []

for c in s:
    if c == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif top == '[':
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp += int(top)
    elif c == "]":
        temp = 0
        while stack:
            top = stack.pop()
            if top == "[":
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp += int(top)
    else:
        stack.append(c)

for c in stack:
    if c == "(" or c == "[":
        print("0")
        exit(0)
    else:
        continue

print(sum(stack))