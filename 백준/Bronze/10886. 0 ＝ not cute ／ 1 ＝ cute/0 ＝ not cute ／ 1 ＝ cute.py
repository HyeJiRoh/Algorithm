n = int(input())
total = 0

for i in range(n) :
    i = int(input())
    if i == 1 :
        total += 1

if (n-total) > n//2 :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")