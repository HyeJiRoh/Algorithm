while True :
  s = input()
  stack = []

  if s == "." :
    break
  
  for i in s :
    if i == '(' or i == '[' :
      stack.append(i)
    elif i == ')' :
      if len(stack) != 0 and stack[-1] == '(' :
        stack.pop()
      else :
        stack.append(')')
    elif i == ']' :
      if len(stack) != 0 and stack[-1] == '[' :
        stack.pop()
      else :
        stack.append(']')

  if len(stack) == 0 :
    print("yes")
  else :
    print("no")
