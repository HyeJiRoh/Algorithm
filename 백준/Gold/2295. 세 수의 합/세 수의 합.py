n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
arr2 = []
for i in range(n):
    for j in range(i, n):
        arr2.append(arr[j] + arr[i])

arr2.sort()
result = 0

for i in range(n):
    for j in range(i, n):
        a = arr[j] - arr[i]
        start = 0
        end = len(arr2) - 1
        while start <= end:
            mid = (start + end) // 2
            b = arr2[mid]
            if a > b:
                start = mid + 1
            elif a < b:
                end = mid - 1
            else:
                result = max(result, arr[j])
                break

print(result)