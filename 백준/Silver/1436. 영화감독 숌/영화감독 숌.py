n = int(input())
arr = []

for i in range(10000001) :
    i = str(i)
    if '666' in i :
        arr.append(i)

print(arr[n-1])