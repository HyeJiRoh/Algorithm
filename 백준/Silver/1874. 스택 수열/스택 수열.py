import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
num = 1
status = True

for i in range(n) :
    i = int(input())

    while num <= i :
        stack.append(num)
        result.append('+')
        num += 1

    if stack[-1] == i :
        stack.pop()
        result.append('-')
    else :
        status = False
        break

if status == True :
    print("\n".join(result))
else :
    print("NO")