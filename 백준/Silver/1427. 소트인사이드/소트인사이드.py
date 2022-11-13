arr = list(input())
result = []

for i in arr :
  result.append(i)

result.sort(reverse = True)

for i in result :
  print(i, end="")