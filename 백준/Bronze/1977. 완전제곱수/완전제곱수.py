m = int(input())
n = int(input())
sqrt = 0
total = 0
min = 10000

for i in range(m, n+1) :
    sqrt = i**0.5
    if i%sqrt == 0 :
        total += i
        if i<min :
            min = i

if total == 0 :
    print(-1)
else :
    print(total)
    print(min)