import sys
input = sys.stdin.readline

str = list(input().strip())
bomb = list(input().strip())
stack = []

for i in range(len(str)):
    stack.append(str[i])

    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))