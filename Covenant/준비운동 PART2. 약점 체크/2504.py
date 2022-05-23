"""
day : 0523
num : 2504
idea : stack
ref : exit(0), 조건을 명확히, ]()에서 올바르지 않은 코드인데 답이 나왔다.
"""

s = input()
stack = []
res = 0

for c in s:
    if c == ')':
        temp = 0
        if stack == []:
            print(0)
            exit(0)
        while stack:
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

for c in stack:
    if c == '(' or c == '[':
        print(0)
        exit(0)
    else:
        res += c

print(res)