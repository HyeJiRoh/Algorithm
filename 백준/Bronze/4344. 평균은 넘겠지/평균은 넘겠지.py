num = int(input())


for i in range(num) :
  arr = list(map(int, input().split()))
  total = 0
  avg = 0
  
  total = sum(arr[1:])
  avg = total/arr[0]
  
  count = 0
  rate = 0

  for k in range(1, len(arr)) :
    if avg < arr[k] :
      count += 1
 
  rate = count/arr[0]
  print(format(rate*100, ".3f")+"%")