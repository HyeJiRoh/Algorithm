arr = []
brr = []

for i in range(3) :
    a = int(input())
    arr.append(a)

for i in range(2) :
    b = int(input())
    brr.append(b)

print(min(arr)+min(brr)-50)