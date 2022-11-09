num, price = map(int, input().split())
coin = []
count = 0

for i in range(num) :
  coin.append(int(input()))  

for i in range(num-1, -1, -1) :
  if price == 0 :
    break

  if price >= coin[i] :
    count += price//coin[i]
    price = price%coin[i]

print(count)