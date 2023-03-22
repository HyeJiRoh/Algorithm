import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = [0 for i in range(n+1)]
arr = []

for i in range(2, n+1) :
    for j in range(i, n+1, i):
        if temp[j] == 0:
            temp[j] = 1
            arr.append(j)
    if len(arr) >= k :
        break

print(arr[k-1])