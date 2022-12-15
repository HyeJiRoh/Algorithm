arr = []
brr = []
result = []

for i in range(3) :
  a, b = map(int, input().split())
  arr.append(a)
  brr.append(b)

for i in arr :
  if arr.count(i) == 1:
    result.append(i)

for i in brr :
  if brr.count(i) == 1:
    result.append(i)

for i in result :
  print(i, end = " ")