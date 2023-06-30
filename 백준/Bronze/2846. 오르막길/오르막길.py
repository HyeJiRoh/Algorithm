n = int(input())
arr = list(map(int,input().split()))

start, end = arr[0], arr[0]

ans = 0

for i in range(1, n):
    if end >= arr[i]:
        start = arr[i]
        end = arr[i]
    else:
        end = arr[i]
    ans = max(ans, end - start)
    
print(ans)