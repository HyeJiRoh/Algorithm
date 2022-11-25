numbers = list(range(1,10_001))
l=[]   

for i in numbers:
    for n in str(i):
        i += int(n)
    if i <= 10_000:
        l.append(i)
      
for k in set(l):
    numbers.remove(k)
  
for result in numbers:
    print(result)