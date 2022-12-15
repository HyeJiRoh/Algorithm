m = int(input())
n = int(input())
arr = []
total = 0
min = 0

for i in range(m, n+1) :
  count = 0
  for k in range(1, i+1) :
    if i%k == 0 :
      count += 1
  if count == 2 :
    arr.append(i)

for i in arr :
  total += i
  
if len(arr) == 0 :
  print(-1)

else : 
  min = arr[0]
  print(total)
  print(min)