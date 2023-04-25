import sys
input = sys.stdin.readline

n = int(input())
arr = input().strip()
num_list = []

for _ in range(n):
    num_list.append(int(input()))

stack = []

for word in arr:
    if word.isalpha():
        word = num_list[(ord(word)-ord('A'))]
        stack.append(word)
    else:
        alpha2 = stack.pop()
        alpha1 = stack.pop()

        if word == '+':
            result = alpha1 + alpha2
        
        elif word == '-':
            result = alpha1 - alpha2
        
        elif word == '*':
            result = alpha1 * alpha2
        
        elif word == '/':
            result = alpha1 / alpha2

        stack.append(result)

print("%.2f" % stack[-1])