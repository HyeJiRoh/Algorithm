s = input().split('-')
arr = []

for i in s :
  result = 0
  n = i.split('+')
  for k in n :
    result += int(k)
  arr.append(result)

a = arr[0]

for i in range(1, len(arr)) :
  a -= arr[i]

print(a)