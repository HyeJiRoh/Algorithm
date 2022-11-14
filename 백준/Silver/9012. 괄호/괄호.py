import sys
input = sys.stdin.readline

num = int(input())

for i in range(num) :
  txt = input()
  arr = []

  for i in txt :
    if i == '(' :
      arr.append(i)
    elif i == ')' :
      if len(arr) == 0 :
        arr.append(i)
        break
      else :
        arr.pop()

  if len(arr) != 0 :
    print("NO")
  else :
    print("YES")