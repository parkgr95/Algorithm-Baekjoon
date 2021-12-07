s = input()
stack = []

for c in s:
    if c == ')':
        temp = 0
        while stack:
            if stack == []:
                print(0)
                exit(0)
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                temp += int(top)
    elif c == ']':
        temp = 0
        if stack == []:
            print(0)
            exit(0)
        while stack:
            top = stack.pop()
            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                temp += int(top)
    else:
        stack.append(c)
for x in stack:
    if x == '(' or x == '[':
        print(0)
        exit(0)

print(sum(stack))

# 회고: ]()에서 올바르지 않은 코드인데 답이 나왔다. 주의할 것