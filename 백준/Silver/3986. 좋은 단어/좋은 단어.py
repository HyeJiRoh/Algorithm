import sys
input = sys.stdin.readline

n = int(input())
result = 0

for _ in range(n):
  stack = []
  word = list(input().strip())
  
  while len(word) > 0:
    str = word.pop()
    if len(stack) == 0:
      stack.append(str)
    else:
      if stack[-1] == str:
        stack.pop()
      else:
        stack.append(str)
  if len(stack) == 0:
    result += 1
    
print(result)
