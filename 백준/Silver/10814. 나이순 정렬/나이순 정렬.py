num = int(input())
arr = []

for i in range(num) :
  age, name = input().split()
  age = int(age)
  arr.append((age, name))

arr.sort(key = lambda text:text[0])

for i in arr :
  print(i[0], i[1])