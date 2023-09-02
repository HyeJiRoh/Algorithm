import sys
input = sys.stdin.readline

S = input()
stack = []

for check in S:
    if check == "(":
        stack.append(check)
    elif check == ")":
        if "(" in stack:
            stack.pop()
        else:
            stack.append(check)

print(len(stack))