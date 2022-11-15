import sys
input = sys.stdin.readline

num = int(input())

for i in range(num) :
  s = input()
  arr = []
  
  for i in s :
    if i == '(' :
      arr.append(i)
    elif i == ')' :
      if '(' not in arr :
        arr.append(i)
        break
      else :
        arr.pop()

  if len(arr) != 0 :
    print("NO")
  else :
    print("YES")