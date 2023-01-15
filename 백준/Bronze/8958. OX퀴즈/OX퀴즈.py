num = int(input())

for i in range(num) :
  arr = list(input())
  count = 0
  total = 0
  
  for k in range(len(arr)):
    if arr[k] == "O" :
      count +=1
      total += count
    else :
      count = 0
  
  print(total)