while True :
  n = int(input())

  if n == 0 :
    break

  count = 0
  for i in range(n+1, n*2+1) :
    result = True
    if i == 1 : 
      continue

    for j in range(2, int(i**0.5)+1) :
      if i%j == 0 :
        result = False
        break
        
    if result : 
      count += 1
  print(count)