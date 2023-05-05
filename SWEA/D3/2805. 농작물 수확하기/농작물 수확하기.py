T = int(input())

for idx in range(1, T + 1):
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(str, input().strip())))

    base = n // 2
    total = 0

    for i in range(0, base + 1):
        for value in arr[i][base:n-base]:
            total += int(value)
        base -= 1
    
    base = 1

    for i in range(n // 2 + 1, n):
        for value in arr[i][base:n-base]:
            total += int(value)
        base += 1
    
    print("#%d %d"%(idx, total))