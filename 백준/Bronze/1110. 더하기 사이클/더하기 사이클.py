num = int(input())

a = num//10
b = num%10

result = b*10+((a+b)%10)

count = 1

while (num != result) :
  a = result//10
  b = result%10

  result = b*10+((a+b)%10) 

  count += 1

print(count)