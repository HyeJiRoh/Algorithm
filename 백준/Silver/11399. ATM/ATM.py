person = int(input())
time = list(map(int, input().split()))
result = 0
time.sort()

total = time[0]
result += total

for i in range(1, person) :
  total = total + time[i]
  result += total

print(result)