N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
total = arr[0]
result = 100001

while True:
    if total < S:
        end += 1
        if end == N: break
        total += arr[end]
    else:
        total -= arr[start]
        result = min(result, end - start + 1)
        start += 1
        
print(result if result != 100001 else 0)