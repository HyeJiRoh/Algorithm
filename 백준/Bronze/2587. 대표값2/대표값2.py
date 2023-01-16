arr = []
avg = 0

for i in range(5) :
    i = int(input())
    arr.append(i)

arr.sort()
print(int(sum(arr)/5))
print(arr[2])