import sys
input = sys.stdin.readline

arr = []
brr = []
for i in range(8) :
    i = int(input())
    arr.append(i)
    brr.append(i)

arr.sort(reverse=True)

print(sum(arr[:5]))

result = []

for i in range(5) :
    result.append(brr.index(arr[i])+1)

result.sort()

for i in result :
    print(i, end=" ")