num = int(input())

for i in range(num) :
  a, b = input().split()
  result = ""
  for k in b :
    result += k*int(a)
  print(result)
  