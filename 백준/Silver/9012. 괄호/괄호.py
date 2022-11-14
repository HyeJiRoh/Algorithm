import sys
input = sys.stdin.readline

t = int(input())

for i in range(t) :
  total = 0
  arr = list(input().strip())

  for i in arr :
    if i == '(':
      total += 1
    elif i == ')' :
      total -= 1
    if total<0 :
      print("NO")
      break
      
  if total == 0 :
    print("YES")
  elif total > 0 :
    print("NO")