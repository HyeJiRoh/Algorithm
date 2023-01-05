total = 0
min = 100

for i in range(7) :
    i = int(input())
    if i%2 !=0 :
        total += i
        if i<min :
            min = i

if total == 0:
    print(-1)
else :
    print(total)
    print(min)