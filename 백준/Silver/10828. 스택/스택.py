import sys
input=sys.stdin.readline

stack = []

num = int(input())

for i in range(num) :
  text = list(input().split())

  if text[0] == "push" :
    stack.append(int(text[1]))
  elif text[0] == "pop" :
    if len(stack) == 0 :
      print(-1)
    else : print(stack.pop())
  elif text[0] == "size" :
    print(len(stack))
  elif text[0] == "empty" :
    if len(stack) == 0 :
      print(1)
    else :
      print(0)
  elif text[0] == "top" :
    if len(stack) == 0 :
      print(-1)
    else :
      print(stack[-1])
    