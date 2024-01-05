import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = list(input().strip())

stack = []

for i in range(len(number)):
    while k > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])

print(''.join(stack[:len(stack)-k]))