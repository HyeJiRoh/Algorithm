n = int(input())
first = 1
max = 6
count = 1
while n > first:
    count += 1
    first += max
    max += 6
print(count)