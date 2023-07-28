import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: -x[2])

print(*arr[0][:2])
print(*arr[1][:2])

i = 2

if arr[0][0] == arr[1][0]:
    while arr[0][0] == arr[i][0]:
        i += 1
print(*arr[i][:2])