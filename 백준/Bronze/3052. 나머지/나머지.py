arr= []
for i in range(10) :
  num = int(input())
  arr.append(num%42)

result = set(arr)
print(len(result))
