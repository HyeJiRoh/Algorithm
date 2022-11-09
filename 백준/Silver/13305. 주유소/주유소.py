num = int(input())

km = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0

for i in range(num-1) :
  if price[i] <= price[i+1] :
    total += price[i] * km[i]
    price[i+1] = price[i]
    
  if price[i] > price[i+1] :
    total += price[i] * km[i]

print(total)