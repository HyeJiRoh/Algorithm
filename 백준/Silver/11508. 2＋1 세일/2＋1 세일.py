import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    i = int(input())
    arr.append(i)

arr.sort(reverse = True)

result = 0

for i in range(n):
    if i % 3 == 2:
        continue
    else:
        result += arr[i]
    
print(result)