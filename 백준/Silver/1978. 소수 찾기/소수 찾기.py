n = int(input())
arr = list(map(int, input().split()))

prime_number = []

for i in range(1, 1001) :
  count = 0
  for k in range(1, 1001) :
    if i%k == 0 :
      count += 1
  if count == 2 :
    prime_number.append(i)

total = 0

for i in arr :
  if i in prime_number :
    total += 1

print(total)