price = int(input())
total = 0

repeat = int(input())
for x in range(repeat) :
  money, count = map(int, input().split())
  total += money*count

if price == total :
  print("Yes")
else :
  print("No")