n = list(input())
stack = []
answer = 0
tmp = 1

for i in range(len(n)):
  if n[i] == '(':
    stack.append(n[i])
    tmp *= 2
  elif n[i] == '[':
    stack.append(n[i])
    tmp *= 3
  elif n[i] == ')':
    if not stack or stack[-1] == '[':
      answer = 0
      break
    if n[i-1] == '(':
      answer += tmp
    stack.pop()
    tmp //= 2
  elif n[i] == ']':
    if not stack or stack[-1] == '(':
      answer = 0
      break
    if n[i-1] == '[':
      answer += tmp
    stack.pop()
    tmp //= 3
    
if stack:
  print(0)
else:
  print(answer)